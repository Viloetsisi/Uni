def isbn_dictionary(filename):
    try:
        book_dict = {}
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                author,title,isbn = line.split(',')
                book_dict[isbn] = (author,title)
        return book_dict
    except FileNotFoundError:
        print("The file " + filename + " was not found.")
        return None
                
            