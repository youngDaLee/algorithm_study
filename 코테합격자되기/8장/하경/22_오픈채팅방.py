'''
user_Id 목록에 대한 해시테이블을 만든다.
==============
key | val
--------------
uid1234  |  Muzi
uid4567   |  Prodo
==============
새로운 사용자가 Enter 할 때 해당 user_Id가 이미 해시테이블에 있거나, 닉네임을 Change 하는 경우
제일 최신 이름으로 val을 다시 써준다. 어찌됐건 최종 닉네임만이 필요하기 때문이다.
'''
def solution(record):
    hash = {}
    res = []

    # 해시테이블 생성
    for state in record:
        state = state.split(" ")
        cmd = state[0]
        user_Id = state[1]

        if cmd == 'Enter' or cmd == 'Change': # 'Leave'인 경우는 무시
            nick = state[2]
            hash[user_Id] = nick

    # 출력문 생성
    for state in record:
        state = state.split(" ")
        cmd = state[0]
        user_Id = state[1]

        if cmd == 'Enter':
            res.append("{0}님이 들어왔습니다.".format(hash[user_Id]))
        elif cmd == 'Leave':
            res.append("{0}님이 나갔습니다.".format(hash[user_Id]))

    return res


record = eval(input())
print(solution(record))
