f = open('1157.txt')
N = list(map(str, f.readline().upper().rstrip()))
# print(N)

l = []
for i in range(65, 91):
    l.append(N.count(chr(i)))
m = max(l)
# print(m)

count = 0
for j in range(0, 26):
    if m == l[j]:
        count += 1

if count >=2:
    print("?")
else:
    print(chr(65 + l.index(m)))