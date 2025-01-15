def find_key(input_dict, value):
    for key,val in input_dict.items():
        if val == value:
            return key
        
    return None
        