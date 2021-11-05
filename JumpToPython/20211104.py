#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 15:03:35 2021

@author: sungahwang
"""

# 클래스
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second 
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
a.setdata(4, 2)
a.add()
a.sub()
a.mul()
a.div()

# 모듈
import mod1
print(mod1.add(3, 4))

from mod1 import add # add 함수만
print(add(3, 4))

from mod1 import add, sub
print(sub(7, 4))

from mod1 import * # 묘듈 안 함수 전체
print(add(3, 4))
print(sub(7, 4))

print(mod1, sub(9, 2))

import pandas as pd

4 / 0 # error
f = open("잘못된 경로, 'r') 
         # error
a = [1, 2, 3]
a[4] # error

a = [5, 4, 3, 2, 1, 0, 2, 3]
for num in a:
    print(1000 / num)
except:
    pass
    
for num in a:
    print(num)

