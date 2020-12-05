#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:11:38 2020

@author: amandahsu
#Special Pythagorean triplet
#https://projecteuler.net/problem=9
"""
#a,b,c is a pythagorean triplet
#a + b + c = 1000
#solve abc

#let a = m^2 + n^2
#    b = 2mn
#    c = m^2 - n^2
#a + b + c = 2(m(m+n))


x = int(input()) #1000

for m in range(int((x/4)**(1/2)), int((x/2)**(1/2)) + 1): #(x/2) ** (1/2) > m > (x/4) ** (1/2)
   for n in range(0, int((x/4)**(1/2)) + 1): # (x/4) ** (1/2) > n > 0
	   
	   if m * (m+n) == x / 2:
		   a = m**2 + n**2
		   b = 2*m*n
		   c = m**2 - n**2
		   break
   
print('Pythagorean triplet is: {a}, {b}, {c}.'.format(a = a, b = b, c = c))

sol = a*b*c
print(sol)
   
