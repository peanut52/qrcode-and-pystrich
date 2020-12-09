# -*-coding:utf-8-*-
# Author: Liu Jing
# Data: 2020  20:24
# File Name: test
# import qrcode
#
# encoder = qrcode.make('http://www.baidu.com')
# encoder.save('baidu.png')
# encoder.show()
import random

print(random.choice('12446578'))
from pystrich.ean13 import EAN13Encoder
encoder = EAN13Encoder('4655343452456')
encoder.save('4655343452456.png')