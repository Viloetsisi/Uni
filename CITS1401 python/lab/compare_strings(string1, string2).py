def compare_strings(string1, string2):
    list1=list(string1)
    list2=list(string2)
    if list1[0] == list2[0]:
        if len(list1) == len(list2):
            return 'error'
        elif len(list1) > len(list2):
            return string1
        else:
            return string2
    elif list1[-1] > list2[-1]:
        return string1
    elif list2[-1] > list1[-1]:
        return string2
    else:
        return 'error'