# 스택

---

## 개념 및 정의

- FILO(First In Last Out) = LIFO(Last In First Out)
- 데이터 추가는 Push, 데이터 추출은 Pop

## ADT(Abstract Data Type)

추상 자료형: 인터페이스만 있고 실제로 구현은 되지 않은 자료형입니다. 일종의 자료형의 설계도

- 언어에 따라 표준 라이브러리에서 스택 제공여부는 다르다. 파이썬의 경우 스택을 제공하진 않지만 대안으로 리스트 함수인 **append( )** 함수, **push( )** 함수로 스택을 대체할 수 있다.
- **덱(deque)**은 한쪽으로만 데이터 삽입, 삭제할 수 있는 스택과 다르게 양쪽에서 데이터를 삽입하거나 삭제할 수 있는 자료구조다. 이런 덱의 특징을 조금만 응용하면 스택처럼 사용할 수 있다.
- 스택에는 ❶푸시(push), ❷팝(pop), ❸가득 찼는지 확인(isFull), ❹비었는지 확인(isEmpty), ❺탑(top) 같은 연산을 정의해야 하지만 Python에서는 다 구현되어 있음...
- 교재에서는 스택의 내부 데이터를 배열로 관리하는 모습을 예로 들었으나, 스택의 원소는 배열이 아니라 다른 자료구조로 관리할 수도 있다.
- 자료구조의 세부구현을 충분히 알면 문제를 어떤 자료구조로 풀어야 하는지 빠르게 파악할 수 있다. 효율적인 알고리즘을 떠올릴 수 있는 것!

## 몸풀기 문제

- [문제] 괄호 짝 맞추기
    - 괄호 짝이 맞으면 True, 맞지 않으면 False
    - Solution: 문자열을 앞에서 하나씩 보며 열린 괄호가 나오면 Push → 닫힌 괄호가 나오면 Pop → 과정을 마지막 문자열까지 반복했는데 스택에 열린 괄호가 남아 있거나 스택이 비었는데 Pop 하려는 경우는 짝이 맞지 않은 것(False)이고, 괄호가 남아 있지 않다면 짝이 맞은 것(True)으로 판단
    - 시간복잡도: 문자열을 순회하며 괄호의 쌍을 확인하므로 시간 복잡도는 O(N)이다. 참고로 괄호 쌍을 확인할 때 append( ) 메서드와 pop( ) 메서드의 시간 복잡도는 O(1)이다.

## 모의테스트

- [문제] ★짝지어 제거하기★
    - 문자열에서 같은 알파벳이 2개 붙어있는 짝을 찾아 앞부터 순서대로 제거한다. 이 과정을 반복하여 최종적으로 모든 문자열을 제거할 수 있다면 1을, 아니면 0을 반환하시오.
    - Solution: ★스택을 떠올리기 힘들지만 스택을 사용하면 굉장히 효율적인 문제. 짝이 맞는 문자를 제거한 다음 문자열을 붙이는 연산은 팝 연산으로 자연스럽게 해결할 수 있음!
    - 시간복잡도: $O(N)$
    - 비고: 이중 for문만 떠올리지 않기. 더욱 효율적인 자료구조와 알고리즘 떠올릴 수 있도록. 물론 이중 for문도 필요하면 써야 한다(입력 데이터 양이 감당할 수 있는 수준이라면).
    
    ```python
    def solution(s):
        stack = []
        for char in s:
            if stack and stack[-1] == char: # 같은 문자가 붙어있으면 pop
                stack.pop()
            else:
                stack.append(char) # 비었거나 문자가 서로 다르면 append
    
        if stack:
            return 0
        else:
            return 1
    
    s = input()
    print(solution(s))
    ```
    
- [문제] 주식 가격
    - 초 단위로 기록된 주식 가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 반환하시오.
    - Solution: 스택에 하나씩 수를 넣어서, 현재 가격이 이전 가격보다 떨어졌다면 길이를 확정하고 pop 실행. 모든 과정이 끝나고 스택에 끝까지 남은 인덱스들의 가격들은 끝까지 떨어지지 않은 것. 따라서 가격을 한 번에 구할 수 있음.
    - 시간복잡도: $O(N)$
    
    ```python
    
    def solution(prices):
    	n = len(prices)
    	answer = [0] * n # ➊ 가격이 떨어지지 않은 기간을 저장할 배열
    	
    	# 스택(stack)을 사용해 이전 가격과 현재 가격을 비교 
    	stack = [0] # ➋ 스택 초기화
    	
    	for i in range(1, n):
    	   while stack and prices[i] < prices[stack[-1]]:
    		 # ➌ 가격이 떨어졌으므로 이전 가격의 기간을 계산
    	       j = stack.pop( )
    	       answer[j] = i - j
    	   stack.append(i)
    	     
    	# ➍ 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우
    	 while stack:
    	     j = stack.pop( )
    	     answer[j] = n - 1 - j
       return answer
    ```
    

- [문제] 크레인 인형 뽑기
    - 크레인을 멈춘 위치에서 가장 위에 있는 인형을 집어올려 바구니에 쌓는다. 이때, 같은 모양의 인형 두 개가 바구니에 연속해 쌓이면 두 인형은 터지며 사라진다. 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 주어질 때, 크레인을 모두 작동시킨 후 사라진 인형 개수를 반환하시오.
    - Solution: board의 컬럼들을 스택으로 만들어 생성함(뽑기 기계에서도 인형들이 팝 되어 없어져야 하므로). moves 인덱스를 따라 숫자를 바구니에 push하고, top과 같은 숫자가 나오면 count +2를 함.
    - 시간복잡도: $O(N^2)$
    - 비고: ★기존 2차원 배열을 스택으로 변환하여 컬럼 단위로 데이터 처리가 가능하도록 만든 케이스!
    
    ```python
    def solution(board, moves):
        stack = [[] for _ in range(len(board))]
        basket = []
        count = 0
    
        for i in range(len(board) - 1, -1, -1): # 각 컬럼마다 스택 생성
            for j in range(len(board)):
                if board[i][j]:
                    stack[j].append(board[i][j])
    
        for i in moves:
            if not stack[i - 1]:  # 스택이 비었을 경우
                pass
            elif not basket or stack[i-1][-1] != basket[-1] and basket: # 바구니가 비었거나 맨 위 인형과 다른 경우
                basket.append(stack[i-1].pop())
            elif basket and stack[i-1][-1] == basket[-1] and basket: # 바구니가 차있고 기존 맨 위 인형과 동일한 경우
                stack[i-1].pop()
                basket.pop()
                count += 2
    
        return count
    
    print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                   [1, 5, 3, 5, 1, 2, 1, 4]))
    ```
    

- [문제] 표 편집
    - - “UX” : 현재 선택한 행에서 X칸 위에 있는 행을 선택합니다.
    - “DX” : 현재 선택한 행에서 X칸 아래에 있는 행을 선택합니다.
    - “C” : 현재 선택한 행을 삭제한 후, 바로 아래행을 선택합니다. 단, 삭제된 행이 가장 마지막 행인 경우 바로 윗행을 선택합니다.
    - “Z” : 가장 최근에 삭제한 행을 원래대로 복구합니다. 단, 현재 선택한 행은 바뀌지않습니다.
    처음 표의 행 개수를 나타내는 정수 n, 처음에 선택한 행의 위치를 나타내는 정수 k, 수행한 명령 어들이 담긴 문자열 배열 cmd가 주어질 때, 모든 명령어를 수행한 후의 표의 상태와 처음 표의 상 태를 비교해 삭제되지 않은 행은 O, 삭제된 행은 X로 표시해 문자열 형태로 반환하시오.
    - Solution: 가장 ‘**최근에**’ 삭제된 행을 복원한다는 점에서 스택을 쓰는 것이 유리함. 기준 위치의 상대적인 위/아래 인덱스로 접근하여, 삭제한 인덱스를 스택에 저장하고 복원할 때 pop 연산 수행.
    - 시간복잡도: $O(N)$
    
    ```python
    def solution(n, k, cmd):
        # ➊ 삭제된 행의 인덱스를 저장하는 리스트
        deleted = [ ]
        # ➋ 링크드리스트에서 각 행 위아래의 행의 인덱스를 저장하는 리스트
        up = [i - 1 for i in range(n + 2)] # 기준이 맨 위일 때를 고려하여 가상 공간 만들기
        down = [i + 1 for i in range(n + 1)] # 기준이 맨 아래일 때를 고려하여 가상 공간 만들기
        # ➌ 현재 위치를 나타내는 인덱스
        k += 1
    
        # ➍ 주어진 명령어(cmd) 리스트를 하나씩 처리
        for cmd_i in cmd:
            # ➎ 현재 위치를 삭제하고 그다음 위치로 이동
            if cmd_i.startswith("C"):
                deleted.append(k) # 삭제된 요소의 인덱스 따로 보관
                up[down[k]] = up[k]
                down[up[k]] = down[k]
                k = up[k] if n < down[k] else down[k] # 맨 마지막 행을 삭제했다면 바로 윗 행 선택
            # ➏ 가장 최근에 삭제된 행을 복원
            elif cmd_i.startswith("Z"):
                restore = deleted.pop()
                down[up[restore]] = restore
                up[down[restore]] = restore
            # ➐ U 또는 D를 사용해 현재 위치를 위아래로 이동
            else:
                action, num = cmd_i.split()
                if action == "U":
                    for _ in range(int(num)): # 숫자만큼 이동
                        k = up[k]
                else:
                    for _ in range(int(num)): # 숫자만큼 이동
                        k = down[k]
    
        # ➑ 삭제된 행의 위치에 'X'를, 그렇지 않은 행의 위치에 'O'를 포함하는 문자열 반환
        answer = ["O"] * n
        for i in deleted:
            answer[i - 1] = "X"
    
        return "".join(answer)
    
    print(solution(8, 2, ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z']))
    print(solution(8, 2, ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z', 'U 1', 'C']))
    ```