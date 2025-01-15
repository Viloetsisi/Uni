def singleDigit(N):
    # Function to add the digits of a number
    def add_digits(num):
        total = 0
        while num > 0:
            total += num % 10
            num //= 10
        return total

    # Base case: if the number is a single digit, return it
    if N < 10:
        return N
    # If the number is not a single digit, add its digits and recurse
    else:
        return singleDigit(add_digits(N))

