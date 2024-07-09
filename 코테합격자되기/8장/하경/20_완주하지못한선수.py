'''
participant 이름들에 대한 해시테이블을 만든다.
==============
key | val
--------------
mislav  |  2
stanko  |  1
ana  |  1
==============
completion 목록에 있는 이름들을 해시테이블에서 -1씩 차감하여, 0 이상 남아있는 이름을 반환한다.
*미완주자는 1명이라고 조건에 명시되어 있음.
'''
def solution(participant, completion):
    hash = {}

    # 해시테이블 생성
    for part in participant:
        if part in hash.keys():
            hash[part] += 1
        else:
            hash[part] = 1

    # 완주자들의 이름을 해시테이블에서 차감
    for comp in completion:
        hash[comp] -= 1

    for not_comp in hash.keys():
        if hash[not_comp] == 1:
            return not_comp


participant = eval(input())
completion = eval(input())
print(solution(participant, completion))