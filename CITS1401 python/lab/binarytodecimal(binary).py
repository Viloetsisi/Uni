def binarytodecimal(binary):
    decimal = 0
    num = len(binary) - 1
    for i in binary:
        if i == '1':
            decimal += 2 ** num
        num -= 1
    return decimal