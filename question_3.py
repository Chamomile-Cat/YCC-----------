"""
3번 문제: 호텔문제
 - 이 호텔은 각 10층이고, 한층에 각각 9개의 방이 있댜.
 - 그래서 10층에 8번째 방이면 방번호 1008이다.
 - 함수는 checkin과 checkout, 두개를 input으로 받습니다, 이때 랜덤하게 손님이 없는 방을 return합니다,

예시)
>>>hotel("checkin")
908호입니다
>>>hotel("checkout", 908)
checkout 되었습니다
"""

"""
코드 계획 (최대한 구체적이게 작성한다) (손으로 작성한다)
호텔 호수를 list로 생성한다 by 층 번호 + 방 개수의 모든 조합, finish
함수 이름은 hotel이다, finish
함수에 checkin이 들어갔을 때랑 checkout이 들어갔을 때랑 달라야 한다. 만약 checkin와 checkout을 1개의 변인으로 받고, room_number가 none인지 아닌지를 보자 , finish) 
만약에 checkin이면 list에서 번호 1개를 주고, 번호를 리스트에서 지운다.
만약에 checkout이면 list에서 호수 번호를 추가한다, "checkout 되었습니다"를 print한다.
"""

import random

floor_number = int(input('How many floors does the hotel have? '))
room_number = int(input('How many rooms on each floor does the hotel have? '))
total_room_number = []
for i in range(1,floor_number+1):
    for j in range(1,room_number+1):
        total_room_number.append(str(i)+'0'+str(j))

def hotel(checkin_or_checkout=None, room_number=None):
    if checkin_or_checkout == "checkin":
        given_room_number = random.choice(total_room_number)
        print('{}호입니다'.format(given_room_number))
        total_room_number.remove(given_room_number)
    if checkin_or_checkout == "checkout" and room_number != None:
        print('checkout 되었습니다')
        total_room_number.append(str(room_number))
        total_room_number.sort()