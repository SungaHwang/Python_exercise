f = open('2657.txt')
N = int(f.readline())
# print(N)

for i in range(0, N):
    S = (f.readline()).split()
    S[0] = int(S[0])
    # print(S)
    num = S[0]
    pr = S[1]
    ans = ""
    for j in range(len(pr)):
        ans += pr[j] * num
    print(ans)
