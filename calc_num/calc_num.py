#!/usr/bin/env python
# -*- coding: utf-8 -*-

# calc_num.py

#不可变参数
# def calc_num(num):
	# sum = 0
	# for n in num:
		# sum = sum + n*n
	# return sum
	
# print calc_num([1,2,3])	
# print calc_num([1,3,5,7])	
# print calc_num([1,2,3,4,5])

#可变参数
def calc_num(*num):
	sum = 0
	for n in num:
		sum = sum + n*n
	return sum
	
Num=[1,2,3]
	
print calc_num(1,2,3)	
print calc_num(1,3,5,7)	
print calc_num(1,2,3,4,5)
print calc_num(Num[0], Num[1], Num[2])
print calc_num(*Num)
