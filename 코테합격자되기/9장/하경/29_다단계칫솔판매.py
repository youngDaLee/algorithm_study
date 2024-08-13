'''
아래와 같은 해시테이블을 생성한다.
==============
enroll | referral
--------------
john   |  -
mary   |  -
...    | ...
young  | edward
==============
재귀함수를 통해 referral을 타고 올라가 수익금을 분배한다.
'''
import math

def distribution(sell, hash, val, result):
    # Assignment
    Q = math.ceil(val * 0.9) # 자기 배당금(90%)
    ref = hash[sell] # 추천인
    keys_list = list(hash.keys()) # 딕셔너리는 Key의 인덱스에 직접접근 할 수 없음...
    self_idx = keys_list.index(sell) # 자기의 인덱스

    # 수행 명령
    result[self_idx] += Q

    # 종료 조건
    if ref == '-': # 끝에 다다르면
        return

    ref_idx = keys_list.index(ref) # 추천인의 인덱스

    # 재귀함수
    distribution(ref, hash, val - Q, result)

def solution(enroll, referral, seller, cost):
    result = [0 * _ for _ in range(len(enroll))]
    hash = {}

    # 해시테이블 생성
    for i in range(len(enroll)):
        hash[enroll[i]] = referral[i]

    # 각 판매금 별로 수익금 분배
    for i, sell in enumerate(seller):
        distribution(sell, hash, cost[i]*100, result)

    return result


enroll = eval(input())
referral = eval(input())
seller = eval(input())
cost = eval(input())

print(solution(enroll, referral, seller, cost))