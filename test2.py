#-*- coding: utf-8 -*-
#file: prime.py

num = int(raw_input('请输入一个数：'))
for i in range (2, num):
    if num % i == 0:
	    print '这个数不是质数！'
		break
	else：
       print '这个数是质数！'
	   