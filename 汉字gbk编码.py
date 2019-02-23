#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 汉字gbk编码.py
# @Author: YC
# @Date  : 2019/1/23
import sys
import requests

#本代码开发环境是Python3.5，在Python2.7未进行测试，有问题请联系我~~~

#汉字转GBK
def utg2GBK(str):
    print(str.encode('gbk'))

	
#GBK转汉字
def gbk2utf(str):
    print('在信息栏中输出  ---  %s'%str.decode('gbk'))


#如果你想把汉字转为GBK编码，那么将下面的 默认 替换为你想转的汉字
utg2GBK('默认'）

#如果你想把汉字转为GBK编码，那么将下面的 b'\xef\xbb\xbf' 替换为你想转的 GBK编码，点击运行
gbk2utf(b'\xef\xbb\xbf')

7