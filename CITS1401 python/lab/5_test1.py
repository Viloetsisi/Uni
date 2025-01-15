def make_dictionary(filename):
    dic = {}
    with open(filename,'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                dic[line] = dic.get(line,0) +1
    return dic