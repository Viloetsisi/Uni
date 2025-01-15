n = int(input())
#Don't change the above line of code. Write your program below this line. Remember to print the final result only.
def fibonacci_sum(n):
    a,b = 0,1
    if n == 1:
        print(0)
    else:
        for i in range(n):
            a,b = b,a+b   
        print(b-1)    
fibonacci_sum(n)