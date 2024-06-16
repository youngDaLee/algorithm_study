"""
문제
* 수포자 3인방이 찍는 방식
    * 1 : [1,2,3,4,5]
    * 2 : [2,1,2,3,2,4,2,5]
    * 3 : [3,3,1,1,2,2,4,4,5,5]
* 가장 많은 문제 맞인 사람 구하기

권장 시간복잡도
* O(N)

내 풀이
* 문제를 O(N)으로 순회하면서
* 해당 Index를 각 배열 크기만큼 나눈것의 나머지 index와 비교
"""

def solution(answer):
    supo_1 = [1,2,3,4,5]
    supo_2 = [2,1,2,3,2,4,2,5]
    supo_3 = [3,3,1,1,2,2,4,4,5,5]

    score = [0,0,0] # 점수

    for i in range(len(answer)):
        idx_1 = i%len(supo_1)
        idx_2 = i%len(supo_2)
        idx_3 = i%len(supo_3)

        if (supo_1[idx_1] == answer[i]):
            score[0] += 1
        if (supo_1[idx_2] == answer[i]):
            score[1] += 1
        if (supo_1[idx_3] == answer[i]):
            score[2] += 1

    max_score = max(score)
    ans = []
    for i in range(3):
        if (max_score == score[i]):
            ans.append(i+1)

    return ans
