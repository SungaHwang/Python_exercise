from unittest import case


H, M = map(int, input().split())
m = int(input())

H_a = (m + M) // 60
M_a = (m + M) % 60

print(f"{(H+H_a) % 24} {M_a}")
