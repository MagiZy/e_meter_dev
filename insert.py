# -*- coding:utf-8 -*-
# ���ַ���str�ĵ�i��λ��֮������ַ�char
def insert(str,i,char):
	l=list(str)
	l.insert(i,char)
	new_str=''.join(l)
	return new_str