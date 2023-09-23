"""
2번 문제
 - import re를 사용합니다. 
 - 문자열을 input으로 받는습니다. 
 - 문자열이 전화번호인지, 사람이름인지, 비밀번호인지(비밀번호는 특수문자, 대문자, 숫자가 모두 포함되어야 함) 구분하는 함수를 제작하자.

"""

"""
코딩 계획을 말로 쓰고 작성하고 구현을 시작하자, 구현 자체보다 코드 디자인이 중요하다.

전화번호: search 시에 '-' & 숫자가 들어가야 한다 
사람이름: search 시에 문자 & 숫자가 없어야 한다
비밀번호: search 시에 특수문자 & 대문자가 나타나야 한다 

"""

import re

def type_of_input():
    user_string = input('Please input your string: ')

    isName = re.compile(r'^[a-zA-Z]+$')
    if isName.match(user_string):
        print('You entered a name.')
        return None
    
    isPhone = re.compile(r'^[0-9]+$')
    temp_str=""
    for i in user_string:
        if i != "-":
            temp_str += i
    if isPhone.match(temp_str):
        print('You entered a phone number.')
        return None
    else: 
        print('You entered a password.')

type_of_input()