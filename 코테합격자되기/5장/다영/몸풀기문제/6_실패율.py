"""
문제
* 실패율 : 스테이지에 도달했으나 아직 클리어 못한 유저 수 / 스테이지 도달한 유저 수
* 전체 스테이지 수 N, 게임 이용 사용자 stages
* 실패율이 높은 스테이지부터 내림차순으로 배열 반환
    * 실패율이 같으면 작은 번호 스테이지가 먼저 오도록

권장 시간복잡도
* O(NlogN)

내 풀이
* hash에 각 스테이지 별 도전자를 저장
* N만큼 순회하면서 스테이지별 실패율 구하기
"""

def solution(n, stages):
    challenger = {i: 0 for i in range(1, n+1)}
    for stage in stages:
        challenger[stage] += 1

    user = len(stages)
    res = {}
    for i in range(1, n+1):
        if challenger[i] == 0:
            res[i] = 0
        else:
            res[i] = challenger[i] / user

        user -= challenger[i]

    return sorted(res, ke=lambda x : res[x], reverse=True)

