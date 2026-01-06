def append_to_list_dangerous(val, my_list=[]):
    my_list.append(val)
    return my_list


def append_to_list(val, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(val)
    return my_list


print(append_to_list_dangerous(1)) # [1]
print(append_to_list_dangerous(2)) # [1,2]
print(append_to_list_dangerous(3)) # [1,2,3]

print(append_to_list(1)) # [1]
print(append_to_list(2)) # [2]
print(append_to_list(3)) # [3]