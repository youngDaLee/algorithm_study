'''
전화번호 배열 phone_book이 다른 번호의 접두어면 False, 그렇지 않으면 True
'''
def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        key1 = phone_book[i]
        key2 = phone_book[i+1]
        if(key1 == key2[:len(key1)]):
            return False
    return True

print(solution(["119", "97674223", "1195524421"] ))
print(solution(["123", "456", "789"]))
print(solution(["12", "123", "1235", "567", "88"]))
