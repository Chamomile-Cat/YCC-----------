
def change_list_to_dict(input_by_user):
    result_dict = {}
    for element in input_by_user:
        if element in result_dict:
            result_dict[element] += 1
        if element not in result_dict:
            result_dict[element] = 1
    print(result_dict)

def change_dict_to_tuple(input_by_user):
    print(tuple(input_by_user))

def change_tuple_to_list(input_by_user):
    print(list(input_by_user))

change_list_to_dict(['bee','cat','tree', 'tree', 'pretty'])
change_dict_to_tuple({'name': 'Lee'})
change_tuple_to_list(('3'))