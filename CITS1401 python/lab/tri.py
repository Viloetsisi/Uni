
print('Please enter the positive numbers for arguments.')
x,y,z = map(eval,input("Enter a length of a triangle's side a,b,c :").split(','))

if (x + y <= z or x + z <= y or y + z <= x):
    print('these three lengths cannot form a triangle.')
else:
    print('these three lengths can form a triangle.')
    if (x == y or x == z or y == z):
        print('these three lengths can form a isosceles triangle.')
    if (x == y == z):
        print('these three lengths can form an equilateral triangle.')
    if (x * x + y * y == z * z or y * y + z * z == x * x or x * x + z * z == y * y):
        print('these three lenghts can form a right triangle.')
