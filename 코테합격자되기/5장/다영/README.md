# 5장. 배열
## 5.1 배열 개념
파이썬에서의 배열 선언
```python
arr = [0,0,0,0,0,0]
arr = [0] * 6
arr = list(range(6))
arr = [0 for _ in range(6)]
```

다차원 배열을 사용할 때도 많지만, 컴퓨터 메모리 구조 상 **차원과 무관하게 메모리에 연속**으로 할당됨

## 5.2 배열 효율성
* 접근(find) : O(1)
  * 임의접근 방식으로 배열 모든 위치 데이터에 한 번에 접근 가능
* 맨 뒤에 삽입(push) : O(1)
* 맨 앞에 삽입 : O(n)
  * 기존 데이터를 뒤로 한 칸씩 밀어야 함.
* 중간 삽입(insert) : O(n)

배열 선택 시 고려할 점
* 임의접근 방식
  * 데이터를 자주 읽어야 하는 경우 Good
  * 메모리 낭비
* 배열로 표현하려는 데이터 너무 많으면 배열 할당에 실패할 수 있음
* insert(중간 삽입) 빈번하면 시간초과 발생 가능

## 5.3 자주 활용하는 리스트 기법
추가
* `append()` : 맨 끝에 추가(push) O(1)
* `+ {list}` : 맨 끝에 추가(push) O(1)
* `insert()` : 특정 위치에 삽입(insert) O(n)

삭제
* `pop(index)` : 특정 위치 데이터 삭제 후 반환 O(1)
* `remove(data)` : 특정 데이터 삭제. 받은 값이 처음 등장하는 위치 데이터를 삭제 O(n)
