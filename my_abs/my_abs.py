#!/usr/bin/env python
# -*- coding: utf-8 -*-

# my_abs.py


def my_abs(x):
	if not isinstance(x, (int,float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x  
	  



print my_abs(-12.45)
#print my_abs('A')