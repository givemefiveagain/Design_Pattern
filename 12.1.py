#!/usr/bin/env python
from abc import ABCMeta,abstractmethod

class Stock1:
    def Sell(self):
        print('sell out stock 1 ')
    def Buy(self):
        print('buy stock 1')
class Stock2:
    def Sell(self):
        print('sell out stock 2 ')
    def Buy(self):
        print('buy stock 2')
class NationalDebt1:
    def Sell(self):
        print('sell out National Debt 1 ')
    def Buy(self):
        print('buy National Debt 1')
        
def main():
    s1 = Stock1()
    s2 = Stock2()
    nd1 = NationalDebt1()
    s1.Buy()
    s2.Buy()
    nd1.Buy()
    s1.Sell()
    s2.Sell()
    nd1.Sell()

if __name__ == '__main__':
    main()
