def add(num):
    digit = 0
    while num > 0:
        digit += num % 10
        num //= 10
    return digit
        
def singleDigit(N):
    if N < 10:
        return N
    else:
        return singleDigit(add(N))
        