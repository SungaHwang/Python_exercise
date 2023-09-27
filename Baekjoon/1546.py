f = open('1546.txt')
N = int(f.readline())

T = (list(map(int,f.readline().rstrip().split())))

M = max(T)

l = []

for i in T:
    new = i/M * 100
    l.append(new)
print(l)

sum = 0
for j in range(0, N):
    sum += l[j]
    mean = sum/N
print(mean)