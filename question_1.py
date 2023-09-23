"""
1번 문제
 - 리스트를 딕셔너리로, 딕셔너리를 튜플로, 튜플을 리스트로 만드는 함수 각각 하나씩 만든다
 - 이때 순서는 고려하지 않는다.
 - 리스트에서 딕셔너리로 만들때에는 리스트의 값이 키가 되고 그 개수가 value가 됩니다.
"""


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