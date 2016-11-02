#!/usr/bin/env python
from abc import ABCMeta,abstractmethod

class AbstractClass:
    __metaclass__ = ABCMeta
    @abstractmethod
    def PrimitiveOperation1(self):
        pass
    @abstractmethod
    def PrimitiveOperation2(self):
        pass
    def TemplateMethod(self):
        self.PrimitiveOperation1()
        self.PrimitiveOperation2()

class ConcreteClassA(AbstractClass):
    def PrimitiveOperation1(self):
        print('Concrete Class A Operation 1')
    def PrimitiveOperation2(self):
        print('Concrete Class A Operation 2')

class ConcreteClassB(AbstractClass):
    def PrimitiveOperation1(self):
        print('Concrete Class B Operation 1')
    def PrimitiveOperation2(self):
        print('Concrete Class B Operation 2')

def main():
    ccA = ConcreteClassA()
    ccB = ConcreteClassB()
    ccA.TemplateMethod()
    ccB.TemplateMethod()

if __name__ == '__main__':
    main()
