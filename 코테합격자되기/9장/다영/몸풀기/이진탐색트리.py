'''
첫번재 인수 lst로 이진탐색트리 생성하고
두번째 인수 search_lst 노드를 이진탐색트리에서 찾을 수 있는지 True, False를 담은 result
'''
class Node:
    '''
    node 클래스
    '''
    def __init__(self, key):
        self.left = None # NODE
        self.right = None # NODE
        self.val = key

class BST:
    def __init__(self):
        self.root = None # NODE

    def insert(self, key):
        # 루트가 비어있으면(첫 삽입) 루트노드로 설정
        if not self.root:
            self.root = Node(key)
            return

        # 삽입하려는 값 위치를 찾아 인서트
        curr = self.root
        while True:
            # 삽입하려는 값이 현재 노드보다 작은 경우 왼쪽 자식 노드로
            if key < curr.val:
                # 왼쪽 자식 노드가 있으면 왼쪽 자식 노드 탐색, 없으면 왼쪽 자식노드로 설정
                if curr.left:
                    curr = curr.left
                else:
                    curr.left = Node(key)
            # 삽입하려는 값이 현재 노드보다 큰 경우 오른쪽 자식 노드로
            else:
                # 오른쪽 자식 노드가 있으면 오른쪽 자식 노드 탐색, 없으면 오른쪽 자식노드로 설정
                if curr.right:
                    curr = curr.right
                else:
                    curr.right = Node(key)

    def search(self, key):
        curr = self.root
        # 탐색하는 값이 존재하지 않거나, 찾을 때 까지 반복
        while curr and curr.val != key:
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr


def solution(lst, search_lst):
    bst = BST()
    for key in lst:
        # 이진탐색트리 생성
        bst.insert(key)

    res = []
    for search_var in search_lst:
        if bst.search(search_var):
            res.append(True)
        else:
            res.append(False)

    return res
