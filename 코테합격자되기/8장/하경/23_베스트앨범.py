'''
총 2개의 해시테이블을 만든다.
1) 장르별 재생 총합
==============
key | val
--------------
classic  |  1450
pop   |  3100
==============
2) 장르별 노래 정보
==============
key | val
--------------
classic  |  [(0, 500), (2, 150), (3, 800)]
pop   |  [(1, 600), (4, 2500)]
==============
1)번 해시테이블을 value 값이 큰 순서대로 정렬하여, 이 순서대로
2)번 해시테이블에 접근해 장르별로 노래 고유번호 두 개씩을 결과에 append 한다.
*2)번 해시테이블의 value 리스트도 재생횟수에 따라 정렬되어야 한다.
'''
def solution(genres, plays):
    total_plays = {}
    songs = {}
    res = []

    # 해시테이블 생성
    for idx, genre in enumerate(genres):
        if genre in total_plays.keys():
            total_plays[genre] += plays[idx]
            songs[genre].append((idx, plays[idx]))
        else:
            total_plays[genre] = plays[idx]
            songs[genre] = [(idx, plays[idx])]

    print(total_plays, songs)

    # 플레이 총합이 큰 장르 순서로 sort
    total_plays_list = sorted(total_plays.items(), key = lambda x:x[1], reverse=True) # 리스트로 반환됨

    # 장르별 노래 정보에 접근하여 탐색
    for genre, _ in total_plays_list:
        # 플레이 횟수가 많은 노래 순서로 sort
        songs_list = sorted(songs[genre], key = lambda x:x[1], reverse=True) # 리스트로 반환됨
        # 두 개의 곡만 append
        res.append(songs_list[0][0])
        res.append(songs_list[1][0])

    return res


genres = eval(input())
plays = eval(input())
print(solution(genres, plays))
