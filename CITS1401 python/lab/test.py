def is_composite(n):
    if n <= 3:
        return False
    if n % 2 == 0:
        return True
    else:
        for num in range(2,n):
            if n % num == 0:
                return True
        return False
