f = open('10818.txt')
N = int(f.readline())

T = (list(map(int,f.readline().rstrip().split())))
# print(T)

Max = max(T)
Min = min(T)

# print(Min)
# print(Max)
Min_str = str(Min)
Max_str = str(Max)

a = ' '
print(Min_str +a+ Max_str)

# b.join(list(map(str, l)))