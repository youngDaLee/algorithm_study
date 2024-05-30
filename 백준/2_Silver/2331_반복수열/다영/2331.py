def main():
    a, p = map(int, input().split())
    d = [a]

    while True:
        num = 0
        for n in list(str(d[-1])):
            num += int(n) ** p

        if num in d:
            print(d.index(num))
            break
        d.append(num)

main()