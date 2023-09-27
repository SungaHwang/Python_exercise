f = open('2562.txt')

l = []
for i in range(1, 10):
    a = i
    l += (list(map(int, f.readline().rstrip().split())))
    # print(l)
    if a == 9:
        #print(l)
        for j in range(0, 9):
            if max(l) == l[j]:
                print(l[j])
                print(j+1)

    
