# -*- coding:utf-8 -*-
from send_data import voltage_send
from send_data import current_send
from send_data import AP_send
from send_data import PF_send
from send_data import fre_send
from send_data import TAP_send
from send_func import rs485


print('voltage data:', rs485(voltage_send))
print('current data:', rs485(current_send))
print('AP data:', rs485(AP_send))
print('PF data:', rs485(PF_send))
print('frequency data:', rs485(fre_send))
print('TAP data:', rs485(TAP_send))
