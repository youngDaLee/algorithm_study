## 스택 구현해보기 

stack = [] 
max_size = 10 # 스택 최대 크기 

def isFull(stack):
    return len(stack) == max_size

# print(isFull(stack))

def isEmpty(stack): 
    return len(stack) == 0 

def push(stack, item): 
    if isFull(stack):
        print("스택이 가득참..")
    else: 
        stack.append(item)
        print("데이터 추가됐어요..")
        
def pop(stack): 
    if isEmpty(stack): 
        print("스택이 비었네요..")
        return None 
    else: 
        return stack.pop()
        
### 파이썬에서는 배열을 선언할때 크기를 정의하지 않으므로 append/pop 만 수행해서 스택 자료형을 사용할 수 있다. 
