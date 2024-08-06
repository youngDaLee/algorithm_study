'''
새로운 파이썬 함수
1.string.startswith(str) -> 문자열이 str으로 시작하는지 판별(boolean)
2.string.endswith(str) -> 문자열이 str으로 끝나는지 판별(boolean)

오름차순으로 정렬한 다음, startswith 함수로 판별하면 됨.
'''
def solution(phone_book):
    phone_book.sort() # 정렬

    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True


phone_book = eval(input())
print(solution(phone_book))