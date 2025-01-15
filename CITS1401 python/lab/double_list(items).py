def double_list(items):
    if len(items) % 2 == 0:
        return(items * 2)
    else:
        new_items = items + [items[-1]]
        return(new_items)
