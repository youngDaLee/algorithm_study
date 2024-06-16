"""
문제
* 행렬 arr1, arr2를 입력받아 arr1에 arr2를 곱한 결고를 반환

권장 시간복잡도
* O(N^2)

내 풀이
* arr1의 col, arr2의 row 크기의 배열 생성
"""

def solution(arr1, arr2):
    col, row = len(arr1), len(arr2[0])
    arr1_row = len(arr1[0])

    ans = [[0]*row for _ in range(col)]
    for i in range(col):
        for j in range(row):
            for arj in range(arr1_row):
                ans[i][j] += arr1[i][arj]*arr2[arj][j]

    return ans

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))