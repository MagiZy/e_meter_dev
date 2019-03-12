# -*- coding:utf-8 -*-
# 在字符串str的第i个位置之后插入字符char
def insert(str,i,char):
	l=list(str)
	l.insert(i,char)
	new_str=''.join(l)
	return new_str