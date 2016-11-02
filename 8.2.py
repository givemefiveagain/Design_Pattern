#!/usr/bin/env python
'''
通过继承实现雷锋工厂
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

if __name__ == '__main__':
    xueleifeng = Leifeng()
    xueleifeng.Sweep()
    xueleifeng.Wash()
    xueleifeng.BuyRice()
    student1 = Undergraduate()
    student1.BuyRice()
    student2 = Undergraduate()
    student2.Sweep()
    student3 = Undergraduate()
    student3.Wash()
