'''
while 루프: 차례
for 루프: 사람
'''
def solution(n, words):
    idx = 0 # 몇 번째 단어인지
    count = 1 # 몇 번째 차례인지
    answer = []
    # 차례 Loop
    while True:
        # 사람 Loop
        for person in range(n): # 몇 번째 사람인지
            # 단어의 앞뒤가 아어지지 않거나, 해당 단어가 앞에 이미 나왔을 때
            if idx > 0 and words[idx][0] != words[idx-1][-1] or words[idx] in words[:idx]:
                answer.append(person+1) # 몇 번째 사람인지 append
                answer.append(count) # 몇 번째 차례인지 append
                return answer
            if idx == len(words) - 1: # 끝까지 다 돌았는데도 위 조건에 걸리지 않는다면
                return [0, 0]
            idx += 1
        count += 1


n = int(input())
words = eval(input())
print(solution(n, words))