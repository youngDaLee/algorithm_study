## 리스트로 큐 구현하기 
from collections import deque

# 큐에 데이터 추가 
queue = [] 
queue.append(1)
queue.append(2)

# 큐의 맨 앞 데이터 제거 
first_item = queue.pop(0)
print(first_item)

## 덱으로 큐 구현하기 
## 

deque = deque() 
deque.append(1)
deque.append(2)

first_item = deque.popleft()
print(first_item)

