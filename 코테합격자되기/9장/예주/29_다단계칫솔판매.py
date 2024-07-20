'''
칫솔판매이익: 10%는 추천인한테 주고, 90%는 내가 먹음 
 -> 10% 는 원단위 절삭, 계산한 금액이 1원 미만이면 내가 다 먹음 
 
 칫솔판매가격: 개당 100원 


enroll - 각 판매원 이름 배열  (center를 제외한 조직 구성원)
referral - 초대시켜준 사람 담긴 배열 
seller - 판매한 판매원 배열 (이름이 중복될 수 있음) 
amount - seller 판매수량 배열 
* 각 판매원이 득한 이익금을 나열한 배열 return  => enroll 순서와 동일하게 리턴한다


example) 
enroll: ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	
referral: ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller: ["young", "john", "tod", "emily", "mary"]	
amount: [12, 4, 2, 5, 10]	
* result: [360, 958, 108, 0, 450, 18, 180, 1080]

특정 값 찾는게 아닌데, 꼭 트리를 구현해야할까?  + 이진트리 형태도 아님 

나의 추천자는 한명임 
딕셔너리 형태 

추천인 딕셔너리 
[
john: -
mary: - 
edward: mary 
sam: edward 
emily: mary
jaimie: mary 
tod: jaimie 
young: edward 
]

판매 딕셔너리
[
young: 1200
john: 400
tod: 200 
emily: 500 
mary: 1000 
] 

-> young 부터 10% 떼서 edward -> mary -> 이렇게 10%떼서 저장 

answer
아니 순서대로 밷어야 하는데 딕셔너리면 어떻게 하지, 일단 고.. 
[]


# 1트 -> 3,6번 케이스만 맞고 나머지 다 틀림 
   ->    sell_dict = dict(zip(seller,list(map(lambda x: x * 100, amount))))  이렇게 판매를 합산하면 안된다.  .. .. 

==> for index, current_seller in enumerate(seller):  로 변경함


# 2트 -> 11,12,13 케이스 시간초과 

'''

def solution1(enroll, referral, seller, amount):
    
    answer = []
    answer_dict = dict(zip(enroll, list([0 for i in range(len(enroll))]))) # 0으로 초기화된 딕셔너리 
    print(answer_dict)
    referral_dict = dict(zip(enroll, referral)) # {'john': '-', 'mary': '-', 'edward': 'mary', 'sam': 'edward', 'emily': 'mary', 'jaimie': 'mary', 'tod': 'jaimie', 'young': 'edward'}  
    sell_dict = dict(zip(seller,list(map(lambda x: x * 100, amount))))  # {'young': 1200, 'john': 400, 'tod': 200, 'emily': 500, 'mary': 1000} 
    
    
    for seller, amount in sell_dict.items(): 
        current_profit = amount
        answer_dict[seller] += (amount - (amount // 10)) # 90 프로 누적 
        parent_seller = seller
        while True: 
            parent_seller = referral_dict[parent_seller] # 
            if parent_seller == "-":  # 종료조건 
                break 
                
            current_profit //= 10 # 10% 
            answer_dict[parent_seller] += (current_profit - (current_profit // 10)) # 90 프로 누적 
            
        # print(seller)
    
    # print(list(answer_dict.values()))
    
    return list(answer_dict.values())
    


def solution2(enroll, referral, seller, amount):
    
    answer_dict = dict(zip(enroll, list([0 for i in range(len(enroll))]))) # 0으로 초기화된 딕셔너리 
    print(answer_dict)
    referral_dict = dict(zip(enroll, referral)) # {'john': '-', 'mary': '-', 'edward': 'mary', 'sam': 'edward', 'emily': 'mary', 'jaimie': 'mary', 'tod': 'jaimie', 'young': 'edward'}  
    # sell_dict = dict(zip(seller,list(map(lambda x: x * 100, amount))))  # {'young': 1200, 'john': 400, 'tod': 200, 'emily': 500, 'mary': 1000} 
    
    for index, current_seller in enumerate(seller): 
        current_profit = amount[index] * 100
        answer_dict[current_seller] += (current_profit - (current_profit // 10)) # 90 프로 누적 
        parent_seller = current_seller
        while True: 
            parent_seller = referral_dict[parent_seller] # 
            if parent_seller == "-":  # 종료조건 
                break 
                
            current_profit //= 10 # 10% 
            answer_dict[parent_seller] += (current_profit - (current_profit // 10)) # 90 프로 누적 
            
        # print(seller)
    
    # print(list(answer_dict.values()))
    
    return list(answer_dict.values())
    

def solution(enroll, referral, seller, amount):
    
    answer_dict = dict(zip(enroll, list([0 for i in range(len(enroll))]))) # 0으로 초기화된 딕셔너리 
    print(answer_dict)
    referral_dict = dict(zip(enroll, referral)) # {'john': '-', 'mary': '-', 'edward': 'mary', 'sam': 'edward', 'emily': 'mary', 'jaimie': 'mary', 'tod': 'jaimie', 'young': 'edward'}  
    # sell_dict = dict(zip(seller,list(map(lambda x: x * 100, amount))))  # {'young': 1200, 'john': 400, 'tod': 200, 'emily': 500, 'mary': 1000} 
    
    for index, current_seller in enumerate(seller): 
        current_profit = amount[index] * 100
        answer_dict[current_seller] += (current_profit - (current_profit // 10)) # 90 프로 누적 
        parent_seller = current_seller
        while True: 
            parent_seller = referral_dict[parent_seller] # 
            if parent_seller == "-":  # 종료조건 
                break 
                
            current_profit //= 10 # 10% 
            answer_dict[parent_seller] += (current_profit - (current_profit // 10)) # 90 프로 누적 
            
            if current_profit <= 0: 
                break
            
        # print(seller)
    
    # print(list(answer_dict.values()))
    
    return list(answer_dict.values())
    



enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]

# print(solution1(enroll,referral,seller,amount))
# print(solution2(enroll,referral,seller,amount))
print(solution(enroll,referral,seller,amount))