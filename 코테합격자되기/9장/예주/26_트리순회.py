'''
전위, 중위, 후위 순회 결과 반환 
[1, 2, 3, 4, 5, 6, 7] [“1 2 4 5 3 6 7”, “4 2 5 1 6 3 7”, “4 5 2 6 7 3 1”] 
'''

# 전위 root - L - R 
def preorder(nodes, idx): 
    if idx < len(nodes): 
        value = str(nodes[idx]) + " " 
        value += preorder(nodes, idx * 2+1) ## 왼쪽 자식노드 
        value += preorder(nodes, idx * 2+2) ## 오른쪽 자식노드
        return value 
    else: 
        return ""

def solution(nodes): 
    
    return preorder(nodes,0)


print(solution([1,2,3,4,5,6,7]))
    
    
