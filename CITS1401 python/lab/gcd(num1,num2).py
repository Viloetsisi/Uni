def gcd(num1,num2):
    if num1 > num2:
        i = num2
    else:
        i = num1
    gcd_number = 1
    for num in range(1,i+1):
        if num1 % num == 0 and num2 % num ==0:
            gcd_number = num
    return gcd_number
            
            
        
        