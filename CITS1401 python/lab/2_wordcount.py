def word_counter(input_str):
    L1 = input_str.lower()
    L2 = L1.split()
    wdict = {}
    for word in L2:
        wdict[word] = wdict.get(word,0) + 1
    return wdict
    