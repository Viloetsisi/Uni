def half_string(string):
    if len(string) % 2 == 0:
        return string[0:int(len(string) / 2 )]
    else:
        return string[0:int((len(string)-1) / 2 )]
