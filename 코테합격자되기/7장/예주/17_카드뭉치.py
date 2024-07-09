'''

• 원하는카드뭉치에서카드를순서대로한장씩사용합니다. 
• 한번사용한카드는다시사용할수없습니다.
• 카드를사용하지않고다음카드로넘어갈수없습니다.
• 기존에주어진카드뭉치의단어순서는바꿀수없습니다.

 1≤cards1의길이,cards2의길이≤10
- 1 ≤ cards1[i]의 길이, cards2[i]의 길이 ≤ 10 - cards1과cards2에는서로다른단어만있음
• 2≤goal의길이≤cards1의길이+cards2의길이
- 1≤goal[i]의길이≤10
- goal의원소는cards1과cards2의원소들로만이루어져있음
• cards1,cards2,goal의문자열들은모두알파벳소문자로만이루어져있음


[“i”, “drink”, “water”] [“want”, “to”] [“i”, “want”, “to”, “drink”, “water”] “Yes”
[“i”, “water”, “drink”] [“want”, “to”] [“i”, “want”, “to”, “drink”, “water”] “No”

어떻게 봐도 큐 문제

'''
from collections import deque

def solution(cards1, cards2, goal):
    answer = ''
    cards1_queue = deque(cards1)
    cards2_queue = deque(cards2)
    goal_queue = deque(goal)
    
    while True: 
        
        if len(goal_queue) == 0:
            answer = "Yes"
            break
        
        current_goal = goal_queue.popleft()    
        
        if cards1_queue and current_goal == cards1_queue[0]:
            cards1_queue.popleft()
        elif cards2_queue and current_goal == cards2_queue[0]:
            cards2_queue.popleft() 
        else: 
            answer = "No"
            break
    print(answer)

solution(["i", "water", "drink"],["want", "to"],["i", "want", "to", "drink", "water"])