n = int(input())
sum_positive_odd = 0

if n > 0:
    for num in range(1, 2 * n + 1):
        if num % 2 != 0:
            sum_positive_odd += num
    print(sum_positive_odd)
else:
    print(0)