def second_half_string(string):
    if len(string) % 2 == 0:
        return string[int(len(string) / 2 ):]
    else:
        return string[int((len(string)-1) / 2 ):]

