def list_sorting(lst1,lst2):
    L = list(zip(lst1,lst2))
    L = sorted(L, key = lambda x:(-x[1],x[0]))
    lst1,lst2 = zip(*L)    
    return list(lst1),list(lst2)