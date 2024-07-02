# 큐
뀨

---

## 개념 및 정의

- FIFO(First In First Out)
- 데이터 추가는 Push, 데이터 추출은 Pop

## ADT(Abstract Data Type)

- 역시나 ❶푸시(push), ❷팝(pop), ❸가득 찼는지 확인(isFull), ❹비었는지 확인(isEmpty), ❺앞(front) ❻뒤(rear) 같은 연산이 필요하고, 구현법은 두 가지.
cf) 메모리 낭비를 줄이고자 원형큐를 사용할 수 있으나 Python에서는 이미 리스트의 길이를 자동으로 관리하기 때문에 필요없음.
    
    1) 리스트 
    
    `pop(0)`으로 맨 앞 데이터 제거
    
    ```python
    queue = [ ]
    
    # 큐에 데이터 추가
     queue.append(1)
     queue.append(2)
     queue.append(3)
     
    # 큐의 맨 앞 데이터 제거
    first_item = queue.pop(0) 
    print(first_item) # 출력: 1
    
    # 큐에 데이터 추가
     queue.append(4)
     queue.append(5)
     
    # 큐의 맨 앞 데이터 제거
    first_item = queue.pop(0) 
    print(first_item) # 출력: 2
    ```
    
    **2) 덱(deque - Double Ended Queue)**
    
    양 끝에서 삽입/삭제할 수 있는 큐
    
    ```python
    from collections import deque
    queue = deque( )
     
     # 큐에 데이터 추가
    queue.append(1)
    queue.append(2)
    queue.append(3)
    
    # 큐의 맨 앞 데이터 제거
    first_item = queue.popleft( )
    print(first_item)  # 1
    
    # 큐에 데이터 추가
    queue.append(4)
    queue.append(5)
    
    # 큐의 맨 앞 데이터 제거
    first_item = queue.popleft( )
    print(first_item)  # 2
    ```
    
    🌟 deque의 수행시간이 훨씬 짧게 걸린다!
    

## 몸풀기 문제

- [문제] 요세푸스 문제
    - N명의 사람들이 원 형태로 서있을 때, 
    - 1번 번호표를 가진 사람을 기준으로 K번째 사람을 없앤다. 
    - 없앤 사람 다음 사람을 기준으로 다시 K번째 사람을 없앤다.
    마지막에 남아있는 사람의 번호를 반환하시오.
    - Solution: 1부터 N까지 숫자를 큐에 넣은 다음, 큐에 남은 숫자 개수가 한 개만 남을 때까지(while) 계속 반복함: K 횟수만큼 큐의 front를 빼고 rear에 넣는 과정을 반복하여, K번째 숫자를 아예 삭제.
    - 시간복잡도: $O(N*K)$

## 모의테스트

- [문제] 기능 개발
    - 진도가 100%일 때 배포되는 기능들이 있다. 각 기능들의 작업 진도가 적힌 정수 배열과 각 작업의 개발 속도가 적힌 정수 배열이 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 반환하시오. 단, 앞의 기능이 100%를 달성하여야 뒤의 기능도 배포될 수 있다.
    - Solution: 각 기능들의 배포 가능일을 구하여, 맨 앞 기능의 배포 가능일보다 일수가 오래 걸리는 기능이 나오면 그 앞까지를 자른다. 이러한 과정을 반복한다.
    - 시간복잡도: $O(N)$
    - 비고: 굳이 큐로 풀지는 않아도 될듯?
    
    ```python
    from collections import deque
    import math
    
    def solution(progress, speed):
        q = deque()
        q_res = deque()
        pre = 0
        count = 0
    
        for idx, val in enumerate(progress):
            q.append(math.ceil((100 - val) / speed[idx])) # 각 진도의 남은 일수
    
        while(q):
            if q[0] > pre: # q[0]과 q.popleft()는 똑같은 값. 맨 앞 기능보다 작업 일수가 오래 걸리면 배포를 나눠준다.
                if count != 0: # 최초 탐색은 제외
                    q_res.append(count)
                count = 1
                pre = q.popleft()
            else:
                q.popleft()
                count += 1
    
            if not q: # 마지막 기능일 때
                q_res.append(count)
    
        return q_res
    
    progress = list(map(int, input().split()))
    speed = list(map(int, input().split(" ")))
    
    print(solution(progress, speed))
    ```
    

- [문제] 카드 뭉치
    - 두 번들의 카드뭉치에서 영어 단어들을 ‘순서대로’ 조합하여, 목표 문장을 만들 수 있으면 Yes, 없으면 No를 반환하시오.
    - Solution: 두 카드뭉치의 단어들을 무조건 ‘앞부터’ 사용해야 한다는 점에서(FIFO) 해당 문제는 큐로 푸는 것이 효율적. goal의 단어들을 cards1, cards2에서도 순서대로 팝하다가, 마지막에 cards 1, 2 모두 비어 있으면 Yes를, 하나라도 남아있으면 No를 반환함.
    - 시간복잡도: $O(N)$
    
    ```python
    from collections import deque
    
    def solution(cards1, cards2, goal):
        cards1 = deque(cards1)
        cards2 = deque(cards2)
        goal = deque(goal)
    
        while(goal): # goal 요소의 개수만큼 반복
            word = goal.popleft()
            if cards1 and cards1[0] == word:
                cards1.popleft()
            if cards2 and cards2[0] == word:
                cards2.popleft()
            print((cards1, cards2))
    
        if len(cards1) == 0 and len(cards2) == 0:
            return True
        else:
            return False
    
    cards1 = list(input().split())
    cards2 = list(input().split())
    goal = list(input().split())
    
    print(solution(cards1, cards2, goal))
    ```