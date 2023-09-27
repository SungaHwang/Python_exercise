f = open('11720.txt')
N = int(f.readline())
# print(N)

l = (list(map(int,f.readline().rstrip())))
# print(l)

sum = 0
for i in range(0, N):
    sum += l[i]
print(sum)