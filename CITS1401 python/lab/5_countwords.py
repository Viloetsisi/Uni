def make_dictionary(filename):
    counts = {}
    with open(filename,'r') as file:
        for line in file:
            line = line.strip()
            if line:
                if line in counts:
                    counts[line] +=1
                else:
                    counts[line] = 1
    return counts
            