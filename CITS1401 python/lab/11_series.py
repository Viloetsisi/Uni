def series(x):
    n = 1/2
    L = 1    
    while n >= x:
        L = L + n
        n = n / 2
        
    return round(L,4)        
    