'''
첫 번째 인수 lst를 이용하여 이진 탐색 트리를 생성하고,
두 번째 인수 search_lst에 있는 각 노 드를 이진 탐색 트리에서 찾을 수 있는지 확인하여
True 또는 False를 담은 리스트 result를 반환 하는 함수 solution( )을 작성

[5, 3, 8, 4, 2, 1, 7, 10] [1, 2, 5, 6] [True, True, True, False] 


'''

### 이진 탐색 트리 생성 
class Node: 
    def __init__(self,key): 
        self.left = None 
        self.right = None 
        self.val = key 
        
        
class BST: 
    def __init__(self): 
        self.root = None
        
    def insert(self, key): 
        # 루트 노드가 없는 경우 새로운 노드가 루트노드 
        if not self.root:
            self.root = Node(key) 
        else: # 적절한 위치에 넣어보자 
            curr = self.root 
            while True: 
                # key가 루트보다 값이 작은 경우
                if key < curr.val: 
                    if curr.left: 
                        curr = curr.left 
                    else: 
                        curr.left = Node(key)
                        break 
                else: #key가 루트보다 값이 큰 경우 
                    if curr.right: 
                        curr = curr.right 
                    else: 
                        curr = Node(key)
                        break 
    
    def search(self, key): 
        curr = self.root 
        while curr and curr.val != key: # 현재 노드가 있고, 찾으려는 키값과 다를때까지 반복
            if key < curr.val: 
                curr = curr.left #왼쪽 자식으로 이동 
            else: 
                curr = curr.right 
        return curr
    
    
def solution(lst, search_lst): 
    bst = BST() 
    # 이진트리 생성 
    for key in lst: 
        bst.insert(key) 
    
    answer = []
    
    for val in search_lst: 
        if bst.search(val):
            answer.append(True)
        else: 
            answer.append(False)
    return answer 

print(solution([3,5,2,6,8],[1,2,6]))

    
    
                
        
        