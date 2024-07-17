'''
배열로 표현된 이진트리의
전위순회, 후위순회, 중위순회 결과를 반환하는 solution 함수
'''


def preorder(tree, idx):
    """
    전위순회
    부모 -> 왼쪽 -> 오른쪽
    루트노드 출력한 뒤, 왼쪽 서브트리 오른쪽 서브트리 재귀호출해서 출력 순서 이어붙임ㄴ
    """
    if idx < len(tree):
        res = str(tree[idx]) + ' '
        res += preorder(tree, idx*2+1) # 왼쪽
        res += preorder(tree, idx*2+2) # 오른쪽
        return res
    else:
        return ''


def inorder(tree, idx):
    """
    중위순회
    왼쪽 -> 부모 -> 오른쪽
    """
    if idx < len(tree):
        res = inorder(tree, idx * 2 + 1) # 왼쪽
        res += str(tree[idx]) + ' ' # 부모
        res += inorder(tree, idx * 2 + 2) # 오른쪽
        return res
    else:
        return ''


def postorder(tree, idx):
    """
    후위순회
    왼쪽 -> 오른쪽 -> 부모
    """
    if idx < len(tree):
        res = inorder(tree, idx * 2 + 1) # 왼쪽
        res += inorder(tree, idx * 2 + 2) # 오른쪽
        res += str(tree[idx]) + ' ' # 부모
        return res
    else:
        return ''


def solution(tree):
    return [
        preorder(tree, 0),
        inorder(tree, 0),
        postorder(tree, 0),
    ]


print(solution([1, 2, 3, 4, 5, 6, 7]))