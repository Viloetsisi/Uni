def odd_finder(a,b,c,d,e,f,g,h,i,j):
    lists = [a,b,c,d,e,f,g,h,i,j]
    count = 0
    for num in lists:
        if num > 0 and num % 2 != 0:
            count += 1
    return count