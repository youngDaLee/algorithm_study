'''
1~n 번호 끝말잇기.
1. 1번부터 한 사람씩 단어 말함
2. 마지막 사람이 단어를 말한 다음 다시 1번부터 시작
3. 앞사람 단어 마지막 문자로 시작하는 단어 말함
4. 이전에 등장한 단어 사용 불가
5. 한글자인 단어 인정 안됨

뱉은 단어 words 줬을 때 가장 먼저 탈락하는 사람 번호와 몇번째 차례에 탈락했는지 반환
탈락자 생기지않으면 [0,0] 리턴
'''
def solution(n, words):
    answer = [0, 0]

    word_set = set()
    for i in range(len(words)):
        if words[i] in word_set or \
            (i > 0 and words[i-1][-1] != words[i][0]):
            return [(i%n)+1,(i//n)+1]
        word_set.add(words[i])

    return answer


print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure"
"establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))