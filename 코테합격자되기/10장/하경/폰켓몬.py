'''
중복을 제거하여 폰켓몬 종류 세기 -> 집합!
고를 폰켓몬의 수와 폰켓몬 종류 개수 둘 중에 더 작은 값을 반환함.
'''
def solution(nums):
    nums_set = set(nums)
    sel_num = int(len(nums)/2) # 고를 폰켓몬의 수

    if sel_num < len(nums_set): # 고를 폰켓몬의 수가 폰켓몬 종류보다 적다면
        return sel_num
    else:
        return len(nums_set)



nums = eval(input())
print(solution(nums))