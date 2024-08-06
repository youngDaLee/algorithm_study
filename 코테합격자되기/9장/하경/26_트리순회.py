'''
요즘에는 BFS, DFS로 푸는 게 더 자연스럽다 보니 BST 방식은 잘 안 쓰지 않나?
- 탐색만 할 거면: BFS, DFS
- 탐색 & 삽입: 이진탐색트리
- 최대/최소: 힙
(중요) 이진트리 != 이진탐색트리
'''

# 부모 -> 왼쪽 자식 -> 오른쪽 자식
def preorder(numbers, idx, visited):
    if idx < len(numbers):
        visited.append(numbers[idx])
        preorder(numbers, 2*idx + 1, visited)  #왼쪽
        '''
        반환되는 변수 visited와 파라미터 visited는 서로 다른 변수(주소값)지만, 
        반환 변수 visited의 값이 결국엔 이전 함수 visited에 assign 된다.
        '''
        preorder(numbers, 2*idx + 2, visited)  #오른쪽
    return visited

# 왼쪽 자식 -> 부모 -> 오른쪽 자식
def inorder(numbers, idx, visited):
    if idx < len(numbers):
        inorder(numbers, 2*idx + 1, visited)    #왼쪽
        visited.append(numbers[idx])
        inorder(numbers, 2*idx + 2, visited)    #오른쪽
    return visited

# 왼쪽 자식 -> 오른쪽 자식 -> 부모
def postorder(numbers, idx, visited):
    if idx < len(numbers):
        postorder(numbers, 2*idx + 1, visited)    #왼쪽
        postorder(numbers, 2*idx + 2, visited)    #오른쪽
        visited.append(numbers[idx])
    return visited


numbers = eval(input())
print(preorder(numbers, 0, []))
print(inorder(numbers, 0, []))
print(postorder(numbers, 0, []))
