#!/usr/bin/env python
from abc import ABCMeta,abstractmethod
from copy import copy

class Prototype:
    __metaclass__ = ABCMeta
    def __init__(self, Id):
        self.__Id = Id
    @property
    def Id(self):
        return self.__Id
    @abstractmethod
    def Clone(self):
        pass

class ConcretePrototype1(Prototype):
    def __init(self,Id):
        super(ConcretePrototype1,self).__init__(self,Id)
    def Clone(self):
        return copy(self)

if __name__ == '__main__':
    p1 = ConcretePrototype1("I")
    c1 = p1.Clone()
    print("Cloned:",c1.Id)
    
