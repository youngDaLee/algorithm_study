a = []
t = int(input())
for _ in range(0, t):
    num = int(input())

    if num == 0:
        if len(a) == 0: # 비었는데 0이면
            print(0)

        else:
            print(min_num) # 뭔가 있는데 0이면
            a.remove(min_num)

    else: # 0 이상의 숫자면
        if len(a) == 0:
            min_num = num
            a.append(num)
        else:
            min_num = min(min_num, num)
            a.append(num)