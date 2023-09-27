f = open('10809.txt')
S = (list((f.readline().rstrip())))
# print(S)
l = len(S)
# print(l)

# a = ord('a')
# z = ord('z')

alp=[]
for i in range(0, 26):
    alp += chr(i + 97)
# print(alp)

for i in range(0, 26):
    success = False
    if i == 25:
        last = True
    else:
        last = False
    for j in range(0, l):
        if alp[i] == S[j]:
            success = True
            if last:
                print(j)
            else:
                print(j, end=' ')
            break
        else:
            continue
    if not success:
        if last:
            print(-1)
        else:
            print(-1, end=' ')
