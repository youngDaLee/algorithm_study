'''
want 목록에 대한 해시테이블을 만든다.
==============
key | val
--------------
banana  |  3
apple   |  2
rice  |  2
pork  |  2
pot  |  1
==============
discount 리스트에 있는 품목들을 해시테이블에서 -1씩 차감하여,
0 초과로 남아있는 품목이 있다면 패스하고 모든 품목이 0 이하라면 카운트를 1 증가한다.
'''
def make_hash(want, number):
    hash = {}

    # 해시테이블 생성
    for idx, w in enumerate(want):
        hash[w] = number[idx]

    return hash

def solution(want, number, discount):
    hash = make_hash(want, number)
    flag = True
    count = 0

    for i in range(len(discount) - 10):
        for j in range(0, 10):
            stuff = discount[i+j]
            # 품목이 hash의 키로 존재하지 않을 때 예외처리
            try:
                hash[stuff] -= 1
            except KeyError as K:
                pass

        for key in hash.keys():
            if hash[key] > 0:
                flag = False
                pass

        if flag == True:
            count += 1

        flag = True

    return count


want = eval(input())
number = eval(input())
discount = eval(input())
print(solution(want, number, discount))