def my_enumerate(items):
    L = []
    count = 0
    for num in items:
        t = (count,num)
        L.append(t)
        count += 1
    return L
        