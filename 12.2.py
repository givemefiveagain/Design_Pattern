#!/usr/bin/env python

class Stock1:
    def sell(self):
        print('sell out stock 1 ')
    def buy(self):
        print('buy stock 1')
class Stock2:
    def sell(self):
        print('sell out stock 2 ')
    def buy(self):
        print('buy stock 2')
class NationalDebt1:
    def sell(self):
        print('sell out National Debt 1 ')
    def buy(self):
        print('buy National Debt 1')
class Realty1:
    def sell(self):
        print('sell out Realty 1 ')
    def buy(self):
        print('buy Realty 1')

class Fund:
    def __init__(self):
        self.s1 = Stock1()
        self.s2 = Stock2()
        self.nd1 = NationalDebt1()
        self.rt1 = Realty1()
    def BuyFund(self):
        self.s1.buy()
        self.s2.buy()
        self.nd1.buy()
        self.rt1.buy()
    def SellFund(self):
        self.s1.sell()
        self.s2.sell()
        self.nd1.sell()
        self.rt1.sell()

def main():
    fd = Fund()
    fd.BuyFund()
    fd.SellFund()
    
if __name__ == '__main__':
    main()
