f = open('4344.txt')
C = int(f.readline())
# print(C)

for i in range(0, C):
    T = list(map(int, f.readline().rstrip().split()))
    # print(T)
    N = T[0]
    # print(N)
    avg = (sum(T) - N) / N
    # print(avg)

    count = 0
    for j in T[1:]:
        if j > avg:
            count += 1
    print('%.3f%%' % ((count / N)*100))
