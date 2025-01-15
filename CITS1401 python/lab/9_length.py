def run_length_encode(nums):
    L = []
    number = None
    count = 0
    for num in nums:
        if number is None or num != number:
            if number is not None:
                L.append((number,count))
            number = num
            count = 1
        else:
            count += 1
    if number is not None:
        L.append((number,count))
    return L
        
            
    
    