def get_name(name_dict, id_num):
    if id_num in name_dict:
        return name_dict[id_num]
    else:
        return None