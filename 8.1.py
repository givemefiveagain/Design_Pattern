#!/usr/bin/env python
import abc
import ast
'''
计算器用工厂模式实现
'''
class OperFactory:
    __metaclass__=abc.ABCMeta
    @abc.abstractmethod
    def CreateOperation(self):
        pass

class AddFactory(OperFactory):
    def CreateOperation(self):
        return OperationAdd()

class SubFactory(OperFactory):
    def CreateOperation(self):
        return OperationSub()

class MultiFactory(OperFactory):
    def CreateOperation(self):
        return OperationMul()

class DiviFactory(OperFactory):
    def CreateOperation(self):
        return OperationDiv()

class Operation:
    def __init__(self):
        self.__numberA=None
        self.__numberB=None    
    @property
    def numberA(self):
        return self.__numberA
    @numberA.setter
    def numberA(self,value):
        self.__numberA=value
        
    @property
    def numberB(self):
        return self.__numberB
    @numberB.setter
    def numberB(self,value):
        self.__numberB=value
    @abc.abstractmethod
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def GetResult(self):
        return self.numberA+self.numberB

class OperationSub(Operation):
    def GetResult(self):
        return self.numberA-self.numberB

class OperationMul(Operation):
    def GetResult(self):
        return self.numberA*self.numberB

class OperationDiv(Operation):
    def GetResult(self):
        if(numberB==0):
            raise Exception ("除数不能为0")
        return self.numberA/self.numberB

if __name__ == '__main__':
    numA = ast.literal_eval(input("请输入数字A: "))
    oper_sympol = input("请输入运算符(+,-,*,/): ")
    operator = {'+':AddFactory(),'-':SubFactory(),'*':MultiFactory(),'/':DiviFactory()}
    factory = operator.get(oper_sympol)
    oper = factory.CreateOperation()
    oper.numberA = numA
    oper.numberB = ast.literal_eval(input("请输入数字B: "))    
    print(oper.GetResult())   
