#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
from math import floor
class CashSuper:
    __metaclass__ = ABCMeta
    @abstractmethod
    def acceptCash(self,money):
        pass

class CashNormal(CashSuper):
    def acceptCash(self, money):
        return money

class CashRebate(CashSuper):
    def __init__(self, moneyRebate):
        self.__moneyRebate = moneyRebate
    def acceptCash(self, money):
        return money * self.__moneyRebate
    
class CashReturn(CashSuper):
    def __init__(self, moneyCondition, moneyReturn):
        self.__moneyCondition = moneyCondition
        self.__moneyReturn = moneyReturn
    def acceptCash(self, money):
        result = money
        if(money >= self.__moneyCondition):
            result = money - floor(money/self.__moneyCondition) * moneyReturn
            return result      


class CashContext:
    def __init__(self, csuper):
        self.__cs = csuper
    def GetResult(self, money):
        return self.__cs.acceptCash(money)

if __name__ == '__main__':
    total = 0.0
    cc = {'正常收费':CashContext(CashNormal()),
          '满300返100':CashContext(CashReturn(300,100)),
          '打8折':CashContext(CashRebate(0.8))}
    
    
