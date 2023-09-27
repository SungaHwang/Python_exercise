# import sys
# f = sys.stdin

f = open('10951.txt')


while True:
    try:
        A, B = (map(int, f.readline().split()))
        print(A + B)
    except:
        exit()


