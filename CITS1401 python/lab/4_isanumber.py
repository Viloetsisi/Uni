def is_a_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False