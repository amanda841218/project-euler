#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:58:30 2020

@author: amandahsu
#Largest palindrome product
#https://projecteuler.net/problem=4
"""
import numpy as np

#a palindromic num is symmetric e.g. 343 or 3553
def check_palindromic_num(num):
	
	num = str(num)
	reverse_num = num[len(num)::-1]
	
	if num == reverse_num:
		return True 
	else:
		return False


digit = 3

#compuute the product of all 3 digit *3 digit numbers
product_base = np.arange(10**(digit-1), 10**digit)

products = list(map(lambda x: x* product_base, product_base))

#flatten the list
products = np.sort(np.concatenate(products).ravel(), axis = False)
products = products[::-1]

#check in reverse the first palindromic num
found = 0
count = 0

while found == 0:
	
	if check_palindromic_num(products[count]) == True:
		found += 1
		sol = products[count]
		
	count += 1

print(sol)


