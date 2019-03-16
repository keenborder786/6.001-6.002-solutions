# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 23:03:57 2018

@author: MMOHTASHIM
"""
x=0
y=0
#for x in range(40):
#  for y in range(40):  
#      if x+y==35 and 2*x+4*y==94:
#          print(str(x)+ " , "+str(y))
#          break
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns


