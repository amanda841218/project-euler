#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 21:32:09 2020

@author: amandahsu
#Sum square difference
#https://projecteuler.net/problem=6
"""

num = int(input())
numList = [i for i in range(1, num+ 1)]   
difArray = map(lambda x: x * (num+x+1)*(num-x)/2, numList)
ssd = 2*sum(difArray)

sol = ssd
print(sol)