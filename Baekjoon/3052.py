f = open('3052.txt')
# print(N)

l = []

for i in range(0, 10):
    N = int(f.readline().rstrip())
    # print(N)
    A = N % 42
    if A not in l:
        l.append(A)
print(len(l))