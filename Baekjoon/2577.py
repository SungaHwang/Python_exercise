f = open('2577.txt')

A = int(f.readline())
B = int(f.readline())
C = int(f.readline())

# print(A)
# print(B)
# print(C)

N = A * B * C
#print(N)

M = (str(N))
# print(M)
# print(len(M))

l =[]
for i in range(0, len(M)):
    l.append(int(M[i]))

for j in range(0, 10):
    print(l.count(j))