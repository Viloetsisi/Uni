def bitshift(s,k,b):
    if b == True:
        return s[k:] + s[:k]
    else:
        return s[-k:] + s[:-k]