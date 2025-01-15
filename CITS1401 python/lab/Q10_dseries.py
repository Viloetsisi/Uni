def dseries(n_terms):
    sum = 0
    for n in range(0,n_terms+1):
        sum = sum + n ** 2
    return(sum)
        
        