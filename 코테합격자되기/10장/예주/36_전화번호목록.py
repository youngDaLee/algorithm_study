'''
전화번호부에 적힌 전화번호 중 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다. 
전화번호가 다음과 같을 경우 구조대 전화번호는 영석이 전화번호 접두사입니다.
• 구조대:119
• 박준영:97674223
• 지영석:1195524421


전화번호부에 적힌 전화번호를 담은 배열 phone_book이 solution( ) 함수의 매개변수로 주어 질 때
어떤 번호가 다른 번호의 접두어이면 False, 
그렇지 않으면 True를 반환하는 solution( ) 함수를 작성해주세요.


startswith -> 현재 문자열이 사용자가 지정하는 특정 문자로 시작하는지 확인하는 메소드
endswith 도 있다 wow ~  
'''

def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book) - 1): 
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    
    
    return True

print(solution(["119", "97674223", "1195524421"]))