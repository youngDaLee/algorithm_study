
'''
1 1번부터번호순서대로한사람씩단어를말합니다.
2 마지막사람이단어를말한다음에는다시1번부터시작합니다.
3 앞사람이말한단어의마지막문자로시작하는단어를말해야합니다. 
4 이전에등장했던단어는사용할수없습니다.
5 한글자인단어는인정되지않습니다.

• 끝말잇기에참여하는사람의수n은2이상10이하의자연수입니다.
• words는끝말잇기에사용한단어들이순서대로들어있는배열이며,길이는n이상100이하입니다.
• 단어의길이는2이상50이하입니다.
• 모든단어는알파벳소문자로만이루어져있습니다.
• 끝말잇기에사용되는단어의뜻(의미)은신경쓰지않으셔도됩니다.
• 정답은[번호,차례]형태로반환해주세요.
• 만약주어진단어들로탈락자가생기지않는다면[0,0]을반환하세요. 

3 
[“tank”, “kick”, “know”, “wheel”, “land”, “dream”, “mother”, “robot”, “tank”]
[3,3]




'''

def solution(n, words):
    person_words = [[] for _ in range(n)]
    already_words = set()

    
    person_n = 0
    person_nth = 0
    last_chr = words[0][0] ## 이전 단어의 마지막글자 를저장 
    for i in range(len(words)):
        ## 사용한 단어x, 이전에 마지막 char랑 지금 단어 첫번째 char가 일치할때만 동작 
        if words[i] not in already_words and last_chr == words[i][0] :
            already_words.add(words[i])
            person_words[i % n].append(words[i])
            last_chr = words[i][-1] 
            print(person_words)
        else:
            person_n = i % n + 1
            person_nth = len(person_words[i % n])+1 
            break
    return [person_n, person_nth]



print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))