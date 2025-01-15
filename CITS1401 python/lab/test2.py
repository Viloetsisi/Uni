def list_sorting(lst1, lst2):
    # Sort the lists simultaneously based on age (descending order) and then by name (ascending order)
    sorted_lists = sorted(zip(lst2, lst1), key=lambda x: (-x[0], x[1]))
    
    # Unzip the sorted lists to get the sorted names and ages separately
    sorted_lst2, sorted_lst1 = zip(*sorted_lists)
    
    # Return the sorted lists
    return list(sorted_lst1), list(sorted_lst2)
