def long_enough(strings,min_length):
    long_string = []
    for string in strings:
        if len(string) >= min_length:
            long_string.append(string)
    return long_string