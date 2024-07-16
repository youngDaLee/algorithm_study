'''
전위, 중위, 후위 순회 결과 반환 
[1, 2, 3, 4, 5, 6, 7] [“1 2 4 5 3 6 7”, “4 2 5 1 6 3 7”, “4 5 2 6 7 3 1”] 
'''

# 전위 root - L - R 
def preorder(nodes, idx): 
    if idx < len(nodes): 
        value = str(nodes[idx]) + " " ## Root 
        value += preorder(nodes, idx * 2+1) ## L 탐색
        value += preorder(nodes, idx * 2+2) ## R 탐색 
        return value 
        # 1 2 4 5 3 6 7
    else: 
        return ""


# 중위 L - Root - R 
def inorder(nodes, idx): 
    if idx < len(nodes): 
        value = inorder(nodes, idx * 2+1) # L 먼저 탐색 
        value += str(nodes[idx]) + " " # 루트 탐색 
        value += inorder(nodes, idx * 2+2) # R탐색 
        return value 
    else: 
        return ""
    
# 후위 L - R - Root 
def postorder(nodes, idx): 
    if idx < len(nodes):
        value = postorder(nodes, idx * 2+1)  
        value = postorder(nodes, idx * 2+2) 
        value = str(nodes[idx]) + " " ## Root 
        return value 
         
    else: 
        return ""
def solution(nodes): 
    
    return preorder(nodes,0)


print(solution([1,2,3,4,5,6,7]))
    
    
