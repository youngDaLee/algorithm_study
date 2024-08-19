import random

# 초기 값 설정
values = ["섬연결", "영어끝말", "전화번호", "폰켓몬", "유니온파인드"]
# peoples = ["다영", "예주", "하경"]
peoples = ["다영", "하경"]

# 결과 딕셔너리 초기화
result = {people: [] for people in peoples}

# 리스트 값을 랜덤하게 셔플
random.shuffle(values)

# 값을 균등하게 분배
for i, value in enumerate(values):
    people = peoples[i % len(peoples)]
    result[people].append(value)

print(result)