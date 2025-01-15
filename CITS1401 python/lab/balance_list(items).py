def balance_list(items):
    if len(items) % 2 == 0:
        return(items)
    else:
        new_items = items + [items[-1]]
        return(new_items)