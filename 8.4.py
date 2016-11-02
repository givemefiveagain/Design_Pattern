#!/usr/bin/env python
import abc
'''
学雷锋的工厂模式
'''
class IFactory:
    __metaclass__=abc.ABCMeta
    @abc.abstractmethod
    def CreateLeiFeng():
        pass

class UndergraduateFactory(IFactory):
    def CreateLeiFeng(self):
        return Undergraduate()

class VolunteerFactory(IFactory):
    def CreateLeiFeng(self):
        return Volunteer()

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

if __name__ == '__main__':
    factory = UndergraduateFactory()
    student = factory.CreateLeiFeng()
    student.BuyRice()
    student.Sweep()
    student.Wash()
