f = open('8958.txt')
N = int(f.readline())
# print(N)



for i in range(0, N):
    T = list(map(str, f.readline().rstrip()))
    # print(T)

    n = 0
    s = 0

    for j in range(0, len(T)):
        if T[j] == 'O':
            n += 1
            for k in range(1, len(T)+1):
                if j-k >= 0:
                    if T[(j-k)] == 'X':
                        break
                    elif T[j] == T[(j-k)] == 'O':
                        s += 1
    # print(s)
    print(n+s)


# 1
# 11
# 111