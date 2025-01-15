def make_dictionary(filename):
    dic = {}
    with open(filename,'r') as file:
        for line in file:
            line = line.strip()
            if line:
                dic[line] = dic.get(line,0) +1
    return dic
            