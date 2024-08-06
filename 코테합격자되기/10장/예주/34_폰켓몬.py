'''
• nums는폰켓몬의종류번호가담긴1차원배열입니다.
• nums의길이(N)는1이상10,000이하의자연수이며항상짝수입니다.
• 폰켓몬의종류번호는1이상200,000이하의자연수입니다.
• 가장많은종류의폰켓몬을선택하는방법이여러가지일때에도,선택할수있는폰켓몬종류
개수의 최댓값 하나만 반환하면 됩니다.

[3, 1, 2, 3] 2 
[3, 3, 3, 2, 2, 4] 3 
[3, 3, 3, 2, 2, 2] 2


엥 그냥 중복제거 하면 되지 않나 
'''

def solution(poketmons): 
    poketmons_set = set(poketmons)  #중복제거 
    n = len(poketmons)  
    select_num = n // 2 
    return min(select_num, len(poketmons_set))

print(solution([3, 3, 3, 2, 2, 2])) 