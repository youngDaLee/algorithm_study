# [10451. 순열 사이클](https://www.acmicpc.net/problem/10451)
## 문제
* 테스트케이스 T, 순열 크기 N
```
1 ... n
사용자입력 순열
```
* 위 형태로 노드 연결이 표현되어 있음 (1 -> 순열[0], 2 -> 순열[1])
* 그래프가 사이클로 표현되는 개수를 찾기
  * dfs로 순회 -> 이미 방문한 노드면 탈출 후 cycle 개수 +1(사이클이라는 뜻)