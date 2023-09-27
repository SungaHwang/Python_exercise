f = open('10871.txt')

N, X = map(int, f.readline().split())
T = (list(map(int,f.readline().rstrip().split())))

# print(N)
# print(X)
# print(T)
# print(T[0])

l = []
for i in range(0, N):
    if T[i] < X:
        l.append(T[i])
    else:
        continue

b = ' '
print(b.join(list(map(str, l))))
