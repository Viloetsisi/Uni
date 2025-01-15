def is_composite(n):
    if n <= 3:
        return False
    if n % 2 ==0 or n % 3 == 0:
        return True
    else:
        for num in range(2,int(n**0.5)+1):
            if n % num == 0:
                return True
        return False
    
def composite2(N):
    count = 0
    num = 9
    while count < N:
        if is_composite(num) and num % 2 != 0:
            count += 1
        num += 2
    return num-2