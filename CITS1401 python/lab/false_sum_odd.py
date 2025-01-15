n = int(input())
sum_positive_odd = 0
if n == 1:
    print(1)
else:
    for s in range(0, n * 2):
        print (s)
        if s % 2 == 0:
            s = 0
        else:
            sum_positive_odd = sum_positive_odd + s
    print(sum_positive_odd)
            