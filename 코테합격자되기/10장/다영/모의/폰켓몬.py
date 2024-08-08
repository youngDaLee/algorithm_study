'''
N마리 포켓몬 중 N/2마리를 가져가도 좋다 -> 같은 종류의 포켓몬을 가질 수도 있다.
N/2 폰켓몬 선택하는 방법 중 가낭 많은 종류 폰켓몬 선택하는 방법
* nums는 항상 짝수

=> 이게 왜 집합문제에..? -> 중복되는 데이터 제거(교집합)
'''
def solution(nums):
    pkm_num = int(len(nums)/2)
    unique = set(nums)
    if len(unique) < pkm_num:
        return len(unique)
    else :
        return pkm_num

print(solution([3, 1, 2, 3]))
print(solution([3, 3, 3, 2, 2, 4]))
print(solution([3, 3, 3, 2, 2, 2]))
