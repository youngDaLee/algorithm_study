'''
arr에서 가장 큰 수의 크기만큼 해시테이블을 만든다.
==============
idx | val
--------------
1  |  1
2  |  1
3  |  1
4  |  1
5  |  0
6  |  0
7  |  0
8  |  1
==============
해시테이블의 인덱스는 각 숫자를 나타내고, 존재하는 수는 1 값을 가진다.
각 원소에 대하여 {target - (원소)}에 해당하는 값이 해시테이블에 있다면 True, 없다면 False
'''
def make_hash(arr):
    hash = [0] * (max(arr) + 1)

    # 해시테이블 생성
    for num in arr:
        hash[num] = 1

    return hash


def solution(arr, target):
    table = make_hash(arr)

    # 각 원소에 대해 탐색
    for num in arr:
        diff = target - num
        if diff != num and table[diff] == 1: # 바로 접근(O(1)). 또한, 대상 숫자가 자기 자신이면 안 됨.
            return True

    return False


arr = eval(input())
target = int(input())
print(solution(arr, target))