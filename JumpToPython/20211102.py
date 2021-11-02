#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:03:27 2021

@author: sungahwang
"""

# 문1
num = 0
sum_num = 0
while num < 1000:
    num += 1
    if num % 3 == 0:
        sum_num += num
        
print(sum_num)

num = 0
sum_num = 0
while num >= 0:
    num += 1
    if num % 3 == 0:
        sum_num += num
    if num >= 1000: break
        
print(sum_num)


# 문2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
for num in numbers:
    if i % 2 == 1:
        result.append(num * 7)
print(result)

for i in range(len(numbers)):
    if numbers[i] % 2 ==1:
        result.append(numbers[i] * 7)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [num * 7 for num in numbers if num % 2 ==1]
print(result) # 앞으로 내포 형식으로 작성


# 함수

def add(a, b): # a, b는 매개변수
    result = a + b
    return result # 기본형(결과값 표시)

'''
def add(a, b):
    return a + b
'''

i = 3
j = 4
k = add(i, j) # addf라는 만든 함수 사용
print(k)


del add # 함수 지우기

def minus(a, b):
    result = a - b
    return result

print(minus(10, 7)) # 매개변수 호출
print(minus(a = 10, b = 7)) # 지정
print(minus(b = 10, a = 7)) #지정하면 순서 바뀌어도 괜찮음

def say():
    return "Hello"

a = say()
print(a) # Hello
    
def minus():
    print("%d에서 %d을 빼면 %d입니다." % (a, b, a - b))

minus(10, 8)
a = minus(10, 8)
print(a) # 2

def say_just():
    print("Hello")
    
a = say_just()
print(a)


# 입력
a = input() 
print(a)
 
# 출력
a = 123
print(a)
a = "Hello"
print(a)
a = [1, 2, 3]
print(a)

print("a" + "b" + "c") # 연결
print("a""b""c") # 연결
print('a''b''c') # 연결

a = "a"
b = "b"
c = "c"

print(a b c) # error
print(a + b + c) # 연결

print(a, b, c) # 한 칸씩 띄어쓰기
print('a', 'b', 'c') # 한 칸씩 띄어쓰기

for i in range(10): # 0~9
    print(i, end = ' ') # 공백 빈칸

for i in range(10): # 0~9
    print(i, end = ',') # 공백 세미콜론


f = open("새파일.txt", 'w') # 파일 생성
f.close() # 파일 닫기

import os
print(os.getcwd()) # working directory 찾기

# 지정된 경로
f = open("/Users/sungahwang/Desktop/python/새파일.txt", 'w')

for i in range(1, 11):
    result = "%d번째 줄\n" % i # 줄 띄우기
    f.write(result) # 파일 안에 임력

f.close

"""
1 - readLine
2 - readLines
3 - read
"""

# 읽기모드
read_f = open("/Users/sungahwang/Desktop/python/새파일.txt", 'r')

line = read_f.readline() # 실행이 될 때 마다 다음줄로 넘어감
print(line)

while True:
    line = read_f.readline()
    if not line: break #더이상 읽어올게 없으면 멈춤
    print(line)

read_f.close()


read_f = open("/Users/sungahwang/Desktop/python/새파일.txt", 'r')

line = read_f.readlines() # 각각의 줄을 요소로 (list)
print(line)

for each_line in line: # 한 줄씩 출력
    print(each_line)

read_f.close()


read_f = open("/Users/sungahwang/Desktop/python/새파일.txt", 'r')

line = read_f.read() # 내용 전체를 뮨저열로
print(line)

read_f.close()
type(line)

read_f = open("/Users/sungahwang/Desktop/python/새파일.txt", 'w')
f.write("Life is too short.") # 작성
f.close()

with open("/Users/sungahwang/Desktop/python/새파일.txt", 'w') as f:
    f.write("Life is too short") #close 안해도 됨



