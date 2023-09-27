f = open('13460.txt')

A, B = (map(int, f.readline().rstrip().split()))
# print(A)
# print(B)

# for i in range(0, A):
#     T = list((f.readline().rstrip()))
#     if 'R' in T:
#         print(i+1)
#     if 'O' in T:
#         print(i+1)
#     if 'B' in T:
#         print(i+1)
    # print(T)

T = []

for i in range(0, A):
    L = list((f.readline().rstrip()))
    T.append(L)
print(T)

for i in range(0, A):
    X_O, Y_O, X_R, Y_R, X_B, Y_B = 0, 0, 0, 0, 0, 0

    if 'O' in T[i]:
        Y_O = i
        X_O = T[i].index('O')
        # print(X_O)
        # print(Y_O)
    
    if 'B' in T[i]:
        Y_B = i
        X_B = T[i].index('B')

    if 'R' in T[i]:
        Y_R = i
        X_R = T[i].index('R')
        # print(X_R)
        # print(Y_R)
            
        try_num = 0

        while True:
            count_R = 0

            if '.' == T[Y_R -1][X_R]:
                print('. on the up side -> current coordinate : ', X_R, Y_R )
                count_R +=1
                T[Y_R][X_R] = '#'
                Y_R = Y_R -1
                try_num +=1
                # if try_num == 10:
                #     print(-1)
                #     break
                if T[Y_R][X_R] == T[Y_O][X_O]:
                    print(try_num)
                    break
                else:
                    continue
            elif '.' == T[Y_R +1][X_R]:
                print('. on the down side -> current coordinate : ', X_R, Y_R )
                count_R +=1
                T[Y_R][X_R] = '#'
                Y_R = Y_R +1
                try_num +=1
                # if try_num == 10:
                #     print(-1)
                #     break
                if T[Y_R][X_R] == T[Y_O][X_O]:
                    print(try_num)
                    break
                else:
                    continue
            elif '.' == T[Y_R][X_R +1]:
                print('. on the right side -> current coordinate : ', X_R, Y_R )
                count_R +=1
                T[Y_R][X_R] = '#'
                X_R = X_R +1
                try_num +=1
                # if try_num == 10:
                #     print(-1)
                #     break
                if T[Y_R][X_R] == T[Y_O][X_O]:
                    print(try_num)
                    break
                else:
                    continue
            elif '.' == T[Y_R][X_R -1]:
                print('. on the left side -> current coordinate : ', X_R, Y_R )
                count_R +=1
                T[Y_R][X_R] = '#'
                X_R = X_R -1
                try_num += 1
                # if try_num == 10:
                #     print(-1)
                #     break
                if T[Y_R][X_R] == T[Y_O][X_O]:
                    print(try_num)
                    break
                else:
                    continue
            else:
                try_num += 1
                break
        print(try_num)



# # find index of R

# # T[[#,#,#,#,#], [#,.,.,B,#], [#,.,#,.,#],[#,R,O,.,#],[#,#,#,#,#]]

# # try = 10

# # A * B -> space
# # initial point of R -> T[3[1]]

# # up side point of initial R -> T[2[1]]
# # down side point of initial R -> T[4[1]]
# # left " -> T[3[0]]
# # right " -> T[3[2]]

# # do not go back

# # if some side- point have . -> move! before #
# # but if the next point has . keep going
# # set up prioity according to the O's point through if...? function
# # (like if O is in more under-side then A, the priority will be under-side direc)

# # B also moves together, count like the same way as A.



# # up, down, right, left
# # stops only in front/before the # -> line 30

