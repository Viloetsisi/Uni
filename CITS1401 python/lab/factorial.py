x = int(input(""))
# Don't change the above line of code. You can assume that x will always be either a positive integer or 0.
factorial = 1
for s in range(1 , x + 1):
    factorial = factorial * s
print(factorial)