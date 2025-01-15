x = int(input())
# Don't change the above line of code. Add your code after this line. Remember not to print anything other than final answer
sum_squares = 0
if x >= 0:
    for s in range(0,x+1):
        sum_squares = sum_squares + s **2
else:
    for s in range(x,0):
        sum_squares = sum_squares + s **2
print(sum_squares)
    