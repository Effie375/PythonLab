
def find_max(max_list):
    index = 0
    max = max_list[index]
    while index < len(max_list):
        if max_list[index] > max:
            max = max_list[index]
        index += 1
    return max


def find_min(min_list):
    index = 0
    min = min_list[index]
    while index < len(min_list):
        if min_list[index] < min:
            min = min_list[index]
        index += 1
    return min


def find_max_idx_val(_list):
    max_index = 0
    index = 0
    while index < len(_list):
        if _list[index] > _list[max_index]:
            max_index = index
        index += 1
    return max_index, _list[max_index]


def find_min_idx_val(_list):
    min_index = 0
    index = 0

    while index < len(_list):
        if _list[index] < _list[min_index]:
            min_index = index
        index += 1
    return min_index, _list[min_index]


def is_Odd(_num):
    if _num % 2:
        return True  # Μονός
    else:
       return False  # Ζυγός
