"""
문제
* 정수 배열 정렬해서 반환하는 solution 함수 작성

권장 시간복잡도
* O(N)

내 풀이
* 내장 함수 .sort() 사용
    * sorted 사용 안 한 이유 : sorted는 새로운 리스트를 생성 -> 메모리 낭비
    * Timsort 알고리즘을 사용해서 O(NlogN) 시간복잡도를 가진다함
"""

li = list()


def solution(li):
    li.sort()
    return li
