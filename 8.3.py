#!/usr/bin/env python
'''
学雷锋的简单工厂模式
'''
class Leifeng:
    def Sweep(self):
        print("扫地")
    def Wash(self):
        print("洗衣")
    def BuyRice(self):
        print("买米")

class Undergraduate(Leifeng):
    pass

class Volunteer(Leifeng):
    pass

class SimpleFactory:
    @staticmethod
    def CreateLeiFeng(str_type):
        leifeng_type = {'学雷锋的大学生':Undergraduate(),'社区志愿者':Volunteer()}
        return leifeng_type.get(str_type)
        
if __name__ == '__main__':
    studentA  = SimpleFactory.CreateLeiFeng('学雷锋的大学生')
    studentA.BuyRice()
    studentB  = SimpleFactory.CreateLeiFeng('学雷锋的大学生')
    studentB.Sweep()
    studentC  = SimpleFactory.CreateLeiFeng('学雷锋的大学生')
    studentC.Wash()
