def run_length_encode(nums):
    if nums != []:
        L = []
        for num in nums:
            t = (num, nums.count(num))
            L.append(t)
            s = set(L)
            L1 = list(s)
            L1.sort(key=lambda x:abs(x[0]))        
        return L1
    else:
        return []
        
