H, M = map(int, input().split())

if M >=45:
    print(f'{H} {M-45}')
elif H>0 and M<45:
    print(f'{H-1} {15+M}')
elif H==0 and M<45:
    print(f'23 {15+M}')
else:
    pass