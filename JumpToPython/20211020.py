#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 22:27:23 2021

@author: sungahwang
"""

a = 1
a
print(a) # 출력을 할때는 print함수를 사용한다.

"""
주석1
주석2
주석3
""" # 여러 줄 주석

a = 123 # 정수
a= -123 # 음수
print(a)
a =1.2 # 실수
print(a) 

a = 3
b = 4
print(a + b) # 합

print(a ** b) # a의 b승

print((a + b) % a) # 나머지 출력
print((a + b) // a) # 몫 출력 

a = "Hello World!" #큰 따움표
print(a)
b = 'Python is fun' # 작은 따움표

c = """Python is very easy". he says.""" # 큰 따움표도 문자로 인식
print(c)

string1 = "Life is too short\nYou need python" # \n줄바꿈
print(string1)
string2 = "Life is too short\tYou need python" # \t tab간격
print(string2)
string3 = "Life is too short\\You need python" # \ 문자열 넣기
print(string3)
string4 = "Life is too short\"You need python" # " 문자열 넣기
print(string4)
string5 = "Life is too short\'You need python" # ' 문자열 넣기
print(string5)

head = "Python"
tail = "R"
print(head + tail) # 문자열 연결
print(head * 3) # 문자열 3번 반복

print("=" * 50) # = 50번 반복
print("Result")
print("=" * 50) # = 50번 반복

string = "Life is too short."
len(string) # 문자열 길이


string[5] # 인덱싱,파이썬은 0번부터 시작함 - i
string[0]
string[17]
string[-1] # 뒤에서부터
string[-5]

string[0] + string[2] + string[2] + string[3]
string[0:4] # 끝 번호보다 하나 더 큰 숫자까지
string[0:3]
string[12:17]
string[-6:-1]
string[7:] # 7부터 끝까지
string[:12] # 처음부터 11까지
string[:] # 전체

str_a = "20211020Rainy"
year = str_a[:4]
month = str_a[4:6]
day = str_a[6:8]
date = str_a[:8]
weather = str_a[8:]
print(year)
print(month)
print(day)
print(date)
print(weather)

a ="Pithon" # 오타
a[1] = "y" # 재할당 불가
a = "Python" # 다시입력
a[:1]
a[2:]
a[:1] + "y" + a[2:] # 재조합

"I eat %d apples." % 3 # 3이 %d 자리에
"I eat %d apples." % "three" # 문자는 불가
"I eat %s apples." % "three" # 문자열

number = 3
"I eat %d apples." % number 

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day) # 두 개

"Ratio is %d." % 2.13 # 정수형으로 바껴짐
"Ratio is %f." % 2.13 # 실수 가능
"Ratio is %s." % 2.13 # 실수 가능

string = "apple"
string.count('p') # p가 몇 개 있는지
string.find('l') # l의 위치
string[3]
string.find('k') # 없으면 -1
string.index('l')
string.index('k') # value error

"a b c d"
" ".join('abcd') # 공백으로 합치기
",".join('abcd') # , 로 합치기
 
a = "hi"
a.upper() # 대문자로 바꾸기

a.upper().lower() # 바로 소문자로 바꾸기

a = "HI"
a.lower() # 소문자로 바꾸기

a = "Life is too short"
a.lower()
a = a.upper() # 재할당
print(a)

a = " hi "
a.lstrip() # 왼쪽 공백 지우기
b = "  hi   "
b.lstrip() # 공백 여러개도 지움
a.rstrip() # 오른쪽 공백 지우기
b.rstrip() # 오른쪽 공백 지우기
a.strip() # 양쪽 공백 지우기
b.strip() # 양쪽 공백 지우기

a = "Pithon"
a.replace("i", "y") # i를 y로
print(a)
a = "apple"
a.replace("p", "b") # 모든 p가 바뀜
a.replace("ap", "ab") # 넓게 지정해서 바꾸기

a = "Life is too short"
a.split() # 공백으로 나누기
b = "a;b;c;d"
b.split(";") # ;로 나누기

# list 자료형
odd = [1, 3, 5, 7, 9]
print(odd)

a = [] #비어있는 list
b = ["a", "b", "c"]
print(b)
c = [1, 2, "a", "b"]
print(c)
d = [1, 2, ["a", "b"]] # 중첩: 대괄호 안에 대괄호
print(d)

c[0] # 첫 번째 값
c[1] # 두번째 값
c[2] # 세번째 값
c[-1] # 마지막 값
c[0] + c[1] # 숫자+ 숫자
c[0] + c[-1] # 숫자와 문자는 불가능 TypeError
c[2] + c[3] # 문자 연결

d[-1] # [] 하나가 요소가 됨
d[2]
d[2][-1] # 요소 안의 요소

a = [1, 2, ['a', 'b', [3, 'c']]]
a[2][2][-1] # 삼중 요소

a[0:2] # slicing
a[:2]
a[2][:2] # indexing 과 slicing

a = [1, 2, 3, 4, 5]
b = a[:2]
c = a[2:]
print(b)
print(c)

a = [1, 2, 3]
b = [4, 5, 6]
a + b # 연결
a * 3 # 3번 반복

len(a) # 길이

a[2] + "hi" # TypeError
str(a[2]) + "hi" # 숫자를 문자로 변환 후 연결

print(a)
a[2] = 4 # 값 수정
print(a)

a.append(4) # list 맨 마지막에 4 추가
a
a.append([5, 6]) # list도 append 가능 -> 이중으로 들어감
a
a = [1, 4, 3, 2]
a.sort() #정렬
a
b = ["b", "c", "d", "a"]
b.sort() # 문자형도 정렬 가능
b

a = [1, 4, 3, 2]
a.reverse() # 역순으로
a
a.sort().reverse() # AttribureError

a.sort()
a.reverse()
a # 내림차순

a.index(2) # 인덱싱 넘버
a.index(0) # 없음 - 오류
a.find(2) # 못씀

a = [1, 2, 4]
a.insert(2, 3) # 2번째에 3이라는 값 넣기
a

a = [1, 2, 3, 1, 2, 3]
a.remove(3) # 첫 번째 3 삭제
a 

a = [1, 2, 3, 1]
a.count(1) # 1이 몇 개 있는지

a = [1, 2, 3]
a.append(4) 
a
a.append(5, 6) # error- 하나의 값만 가능
a
a.extend([5,6]) # 대괄호 이용, 연결
a

a = a + [7, 8] # extend와 같음
a

a += [7, 8] # 위와 같음
a

a = 0

a = a+7
a

a+= 7
a

# 튜플 자료형
t1 = (1, 2, 3) # 괄호로
print(t1) # 여러 줄 동시 출력을 위해 print쓰는게 좋음

t2 = (1,) # 하나의 값만 입력할 때는 뒤에 쉼표
print(t2)

l1 = [1] # list는 그냥 하나
print(l1)

t3 = 1, 2, 3 # 괄호 생략 가능
print(t3)

t4 = (1, 2, ('a', "b"))
t4

l4 = [1, 2, ["a", "b"]]
l4
l4[1] = 3
l4

t4[1] = 3 # 튜플은 리스트와 다르게 수정 불가능

len(t4) # 길이

# working directory
import os
os.getcwd()
