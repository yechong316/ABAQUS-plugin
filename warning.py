# coding:utf-8 

# 导入ABAQUS必备的方法包
from abaqus import *
from abaqusConstants import *

def warning(num):
    mat_name = mdb.models['Model-1'].Material(name="composite")
    mat_name.Density(table=((num,),))
