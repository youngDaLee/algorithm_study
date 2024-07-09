'''
string_list 단어들에 대한 해시테이블을 만든다.
==============
key | val
--------------
apple   |  1
banana  |  1
cherry  |  1
==============
query_list에 있는 단어들이 해시테이블에 있는지 탐색한다(O(1)).
'''
def solution(string_list, query_list):
    hash = {}
    res = []

    # 해시테이블 생성
    for str in string_list:
        hash[str] = 1

    for query in query_list:
        # query라는 단어가 hash의 키로 존재하지 않을 때 예외처리
        try:
            if hash[query] == 1: # 존재함.
                res.append(True)
        except KeyError as K: # 존재하지 않음.
            res.append(False)

    return res


string_list = eval(input())
query_list = eval(input())
print(solution(string_list, query_list))
