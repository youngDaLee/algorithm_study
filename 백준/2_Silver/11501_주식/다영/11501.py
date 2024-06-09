def stock(n, stock_li):
    """
    """
    res = 0
    s = 0
    for i in range(n-1, -1, -1):
        s = max(stock_li[i], s)
        if (s-stock_li[i] > 0):
            res += s-stock_li[i]

    return res


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stock_li = list(map(int, input().split()))
        print(stock(n, stock_li))


main()
