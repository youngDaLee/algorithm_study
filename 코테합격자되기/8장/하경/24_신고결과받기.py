'''
총 2개의 해시테이블을 만든다.
1) 인원별 신고 목록
==============
key | val
--------------
Muzi  |  [Frodo, Neo]
Frodo   |  [Neo]
Apeach  | [Muzi, Frodo]
Neo  |  [None]
==============
2) 인원별 신고 누적 목록
==============
key | val
--------------
Muzi  |  1
Frodo   |  2
Apeach  |  0
Neo  |  2
==============
2)번 테이블에서 신고횟수를 초과한 사람들을 찾아, 1)번 테이블의 val와 교집합 개수를 찾아낸다.
'''
def make_hash(id_list, report):
    report_list = {}
    report_count = {}

    # report_list 해시테이블
    for id in id_list:
        report_list[id] = []
    for rep in report:
        rep = rep.split(" ")
        report_list[rep[0]].append(rep[1])

    #report_count 해시테이블
    for id in id_list:
        report_count[id] = 0
    for rep in report:
        rep = rep.split(" ")
        report_count[rep[1]] += 1

    return (report_list, report_count)

def solution(id_list, report, k):
    reportees = []
    answer = []
    report_list, report_count = make_hash(id_list, report)
    print(report_list, report_count)

    # 누적 신고 횟수 초과자들
    for reportee in report_count.keys():
        if report_count[reportee] >= k:
            reportees.append(reportee)

    # 신고자 목록과의 교집합 개수 구하기
    for reporter in report_list.keys():
        intersection = list(set(report_list[reporter]) & set(reportees)) # set 자료형으로 변환하여 교집합 구하기
        answer.append(len(intersection))

    return answer

id_list = eval(input())
report = eval(input())
print(solution(id_list, report, 2))
