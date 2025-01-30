//  CITS2002 Project 2 2024
//  Student:   24194872   Mengxi Li
//  Platform:   Linux

/* Assumption
   1. The string "Empty" is printed when the program is displaying the contents of RAM
      and encounters a memory unit that is not occupied by any page.
   2. The input file should contain only one line of input. The program will output an error message
      "Error: Input file contains multiple lines" and exit with EXIT_FAILURE if more than one line is detected.
   3. If the input file is empty, the program outputs "Error: the file is empty" and exits with EXIT_FAILURE.
   4. We will load the process again when we call the process more than 4 times.
   5. When input file contains any non-numeric characters, the program outputs "Error: Invalid input in file" and exists
      with EXIT_FAILURE.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PAGE_SIZE 2           // Size of each page in memory units
#define NUM_FRAMES 8          // Number of frames in RAM
#define NUM_PROCESSES 4       // Total number of processes
#define PAGES_PER_PROCESS 4   // Number of pages per process
#define FRAME_NOT_IN_RAM 99   // Indicator that the page is not in RAM
#define RAM_SIZE  16          // Total number of memory units in RAM (NUM_FRAMES * PAGE_SIZE)
#define VM_SIZE   32          // Total number of memory units in virtual memory (NUM_PROCESSES * PAGES_PER_PROCESS * PAGE_SIZE)

// Structure to represent a page in memory
typedef struct {
    int process_id;     // ID of the process that owns the page
    int page_num;       // Page number within the process
    int last_accessed;  // Time step when the page was last accessed
} memory;

// Structure to represent a process control block (PCB)
typedef struct {
    int page_table[PAGES_PER_PROCESS]; // Page table for the process mapping pages to frames
    int next_page_to_load;             // Index of the next page to be loaded for the process
} process_control_block;

memory* RAM[RAM_SIZE];   // Array of pointers representing RAM memory units
memory* VM[VM_SIZE];     // Array of pointers representing virtual memory units
process_control_block PCB[NUM_PROCESSES]; // Array of PCBs for all processes

int time_step = 0; // Simulation time step counter

// Function prototypes
void initialize_virtual_memory();
void initialize_RAM();
void load_page(int process_id);
int find_free_frame();
int find_LRU_frame_global();
int find_LRU_frame_local(int process_id);
void print_page_tables(FILE* fp);
void print_RAM_contents(FILE* fp);

// Function to initialize virtual memory with pages for all processes
void initialize_virtual_memory() {
    int index = 0; // Index to keep track of positions in VM array

    // Loop over each process
    for (int pid = 0; pid < NUM_PROCESSES; pid++) {
        // Loop over each page for the current process
        for (int page_num = 0; page_num < PAGES_PER_PROCESS; page_num++) {
            // Allocate memory for a new page
            memory* page = (memory*)malloc(sizeof(memory));
            page->process_id = pid;    // Set the process ID
            page->page_num = page_num; // Set the page number
            page->last_accessed = 0;   // Initialize last accessed time to 0

            // Each page occupies PAGE_SIZE consecutive locations in VM
            VM[index++] = page;        // Point to the page struct
            VM[index++] = page;        // Point to the same page struct (since PAGE_SIZE = 2)
        }
    }
}

// Function to initialize RAM by setting all memory units to NULL (empty)
void initialize_RAM() {
    for (int i = 0; i < RAM_SIZE; i++) {
        RAM[i] = NULL; // Mark each memory unit as empty
    }
}

// Function to load a page into RAM for a given process
void load_page(int process_id) {
    // Determine the page number to load based on next_page_to_load modulo PAGES_PER_PROCESS
    int page_num = PCB[process_id].next_page_to_load % PAGES_PER_PROCESS;

    // Check if the page is already in RAM by looking at the page table
    if (PCB[process_id].page_table[page_num] != FRAME_NOT_IN_RAM) {
        // Page is already in RAM; update its last accessed time
        int frame_number = PCB[process_id].page_table[page_num]; // Get the frame number from the page table
        int ram_index = frame_number * PAGE_SIZE;                // Calculate the starting index in RAM
        RAM[ram_index]->last_accessed = time_step;               // Update last accessed time
    } else {
        // Page is not in RAM; need to load it
        int frame_number = find_free_frame(); // Try to find a free frame in RAM

        if (frame_number == -1) {
            // No free frame available; use the LRU replacement algorithm
            frame_number = find_LRU_frame_local(process_id); // Try local LRU first

            if (frame_number == -1) {
                // No pages of this process are in RAM; use global LRU
                frame_number = find_LRU_frame_global();
            }

            // Evict the page currently in the selected frame
            int evicted_ram_index = frame_number * PAGE_SIZE; // Calculate index of the frame to evict
            memory* evicted_page = RAM[evicted_ram_index];    // Get the evicted page

            // Update the page table of the process that owned the evicted page
            PCB[evicted_page->process_id].page_table[evicted_page->page_num] = FRAME_NOT_IN_RAM;
        }

        // Load the new page into the selected frame in RAM
        int ram_index = frame_number * PAGE_SIZE;                           // Calculate the starting index in RAM
        int vm_index = (process_id * PAGES_PER_PROCESS + page_num) * PAGE_SIZE; // Calculate the index in VM

        // Copy the page from virtual memory to RAM
        RAM[ram_index] = VM[vm_index];           // First memory unit of the page
        RAM[ram_index + 1] = VM[vm_index + 1];   // Second memory unit of the page (points to the same struct)

        // Update the last accessed time for the loaded page
        RAM[ram_index]->last_accessed = time_step;

        // Update the page table to reflect that the page is now in RAM
        PCB[process_id].page_table[page_num] = frame_number;
    }

    // Move to the next page to load for this process
    PCB[process_id].next_page_to_load++;
}

// Function to find a free frame in RAM
int find_free_frame() {
    // Iterate over all frames in RAM
    for (int frame = 0; frame < NUM_FRAMES; frame++) {
        int ram_index = frame * PAGE_SIZE; // Calculate starting index of the frame in RAM
        if (RAM[ram_index] == NULL) {
            // Found a free frame
            return frame;
        }
    }
    // No free frames found
    return -1;
}

// Function to find the Least Recently Used (LRU) frame globally across all processes
int find_LRU_frame_global() {
    int min_time = time_step; // Initialize minimum time to current time step
    int lru_frame = -1;       // Initialize LRU frame index

    // Iterate over all frames in RAM
    for (int frame = 0; frame < NUM_FRAMES; frame++) {
        int ram_index = frame * PAGE_SIZE; // Calculate starting index of the frame in RAM
        if (RAM[ram_index] != NULL) {
            // Check if this page was accessed earlier than the current minimum
            if (RAM[ram_index]->last_accessed < min_time) {
                min_time = RAM[ram_index]->last_accessed; // Update minimum time
                lru_frame = frame;                        // Update LRU frame index
            }
        }
    }

    return lru_frame; // Return the frame number of the LRU page
}

// Function to find the Least Recently Used (LRU) frame within the same process (local LRU)
int find_LRU_frame_local(int process_id) {
    int min_time = time_step; // Initialize minimum time to current time step
    int lru_frame = -1;       // Initialize LRU frame index
    int found = 0;            // Flag to indicate if any pages of the process are in RAM

    // Iterate over all frames in RAM
    for (int frame = 0; frame < NUM_FRAMES; frame++) {
        int ram_index = frame * PAGE_SIZE; // Calculate starting index of the frame in RAM
        if (RAM[ram_index] != NULL && RAM[ram_index]->process_id == process_id) {
            // Found a page belonging to the process in RAM
            found = 1;
            if (RAM[ram_index]->last_accessed < min_time) {
                min_time = RAM[ram_index]->last_accessed; // Update minimum time
                lru_frame = frame;                        // Update LRU frame index
            }
        }
    }

    if (found)
        return lru_frame; // Return the frame number of the LRU page of the process
    else
        return -1;        // No pages of this process in RAM
}

// Function to print the page tables of all processes to the output file
void print_page_tables(FILE* fp) {
    // Iterate over all processes
    for (int pid = 0; pid < NUM_PROCESSES; pid++) {
        // Iterate over all pages of the process
        for (int page_num = 0; page_num < PAGES_PER_PROCESS; page_num++) {
            fprintf(fp, "%d", PCB[pid].page_table[page_num]); // Print the frame number or FRAME_NOT_IN_RAM
            if (page_num < PAGES_PER_PROCESS - 1)
                fprintf(fp, ","); // Separator between page table entries
        }
        fprintf(fp, "\n"); // Newline after each process's page table
    }
}

// Function to print the contents of RAM to the output file
void print_RAM_contents(FILE* fp) {
    // Iterate over all memory units in RAM
    for (int i = 0; i < RAM_SIZE; i++) {
        if (RAM[i] != NULL) {
            // Memory unit is occupied; print process ID, page number, and last accessed time
            fprintf(fp, "%d,%d,%d", RAM[i]->process_id, RAM[i]->page_num, RAM[i]->last_accessed);
        } else {
            // Memory unit is empty
            fprintf(fp, "Empty");
        }

        if (i < RAM_SIZE - 1)
            fprintf(fp, "; "); // Separator between memory units
    }
    fprintf(fp, "\n"); // Newline after printing all RAM contents
}

// Main function
int main(int argc, char* argv[]) {
    // Check if the correct number of command-line arguments are provided
    if (argc != 3) {
        printf("Usage: simulation in.txt out.txt\n");
        exit(EXIT_FAILURE);
    }

    char* input_file = argv[1];  // Input file name (process IDs)
    char* output_file = argv[2]; // Output file name (page tables and RAM contents)

    // Initialize virtual memory and RAM
    initialize_virtual_memory();
    initialize_RAM();

    // Initialize process control blocks (PCBs)
    for (int i = 0; i < NUM_PROCESSES; i++) {
        // Initialize page table entries to indicate pages are not in RAM
        for (int j = 0; j < PAGES_PER_PROCESS; j++) {
            PCB[i].page_table[j] = FRAME_NOT_IN_RAM;
        }
        PCB[i].next_page_to_load = 0; // Start with the first page for each process
    }

    // Open the input file for reading
    FILE* fp_in = fopen(input_file, "r");
    if (!fp_in) {
        printf("Error: Cannot open input file %s\n", input_file);
        exit(EXIT_FAILURE);
    }

    // Check if the input file is empty
    fseek(fp_in, 0, SEEK_END);          // Move file pointer to the end
    long file_size = ftell(fp_in);      // Get the size of the file
    if (file_size == 0) {
        printf("Error: the file is empty.\n");
        fclose(fp_in);
        exit(EXIT_FAILURE);
    }
    rewind(fp_in); // Reset file pointer to the beginning

    // Check for multiple lines in the input file
    int c;
    int line_count = 0;
    while ((c = fgetc(fp_in)) != EOF) {
        if (c == '\n') {
            line_count++;
        }
    }
    rewind(fp_in); // Reset file pointer to the beginning

    if (line_count > 0) {
        // More than one line detected
        printf("Error: Input file contains multiple lines\n");
        fclose(fp_in);
        exit(EXIT_FAILURE);
    }

    // Read process IDs from the input file and simulate page loading
    int process_id;
    int scan_result;
    while ((scan_result = fscanf(fp_in, "%d", &process_id)) != EOF) {
        if (scan_result == 0) {
            // Non-integer input encountered
            printf("Error: Invalid input in file\n");
            fclose(fp_in);
            exit(EXIT_FAILURE);
        }
        if (process_id < 0 || process_id >= NUM_PROCESSES) {
            // Invalid process ID detected
            printf("Error: Invalid process ID %d\n", process_id);
            fclose(fp_in);
            exit(EXIT_FAILURE);
        }

        // Load the page for the given process ID
        load_page(process_id);
        time_step++; // Increment the time step after each page load
    }

    fclose(fp_in); // Close the input file

    // Open the output file for writing
    FILE* fp_out = fopen(output_file, "w");
    if (!fp_out) {
        printf("Error: Cannot open output file %s\n", output_file);
        exit(EXIT_FAILURE);
    }

    // Print the page tables and RAM contents to the output file
    print_page_tables(fp_out);
    print_RAM_contents(fp_out);

    fclose(fp_out); // Close the output file

    // Free allocated memory for virtual memory pages
    for (int i = 0; i < VM_SIZE; i += PAGE_SIZE) {
        if (VM[i]) {
            free(VM[i]); // Free the allocated memory
            VM[i] = NULL;
        }
    }

    return 0; // Program executed successfully
}
