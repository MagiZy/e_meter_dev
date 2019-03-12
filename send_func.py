# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import time
from insert import insert
from struct import unpack


def rs485(send):
	EN_485 = 4
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(EN_485, GPIO.OUT)
    GPIO.output(EN_485, GPIO.HIGH)

    t = serial.Serial("/dev/ttyS0", 9600, parity='N', timeout=1)
  
    while 1:
        # set the rs485 as the send mode
        print('----- send data -----')
        GPIO.output(EN_485, GPIO.HIGH)
        t.write(send)
        time.sleep(2)
        # set the rs485 as the receive mode
        GPIO.output(EN_485, GPIO.LOW)
        receive = t.read(9)
        print('----- receive data -----')
		str1=receive[3:7]	# 取接收字符串的第3-6个数据字符
		new_str = ''
		for index in range(len(str1)):
			if ord(str1[index])<=15:	#如果该位字符的ASCII码值小于16
				new_str += insert(str(hex(ord(str1[index]))),2,'0')[2:4]	# 在该位字符ASCII码十六进制字符串的'0x'后添0，以保证有两位数据位，并取出该两位数据
			else:														# 例如'0x6'-->'0x06'-->'06'
				new_str += str(hex(ord(str1[index])))[2:4]	# 拼接数据字符串
		#print('----- float data -----')
		print(unpack('>f', (new_str.decode('hex'))))	# 输出十六进制数据对应的浮点数
		#print('----- float data -----')
        #for i in receive:
        #    print('%#x' % ord(i))
