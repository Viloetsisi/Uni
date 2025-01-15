def duplicate_last(data):
    newlist = data[:]
    newlist.append(data[-1])
    return newlist