#!/usr/bin/env python
from abc import ABCMeta,abstractmethod

class Flyweight:
    __metaclass__ = ABCMeta
    @abstractmethod
    def Operation(self, extrinsicstate):
        pass
    
class ConcreteFlyweight(Flyweight):
    def Operation(self, extrinsicstate):
        print('concrete Flyweight:',extrinsicstate)

class UnShareConcreteFlyweight(Flyweight):
    def Operation(self, extrinsicstate):
        print('unshared concrete Flyweight:',extrinsicstate)

class FlyweightFactory:
    def __init__(self):
        self.__flyweights = dict()
        self.__flyweights['X'] = ConcreteFlyweight()
        self.__flyweights['Y'] = ConcreteFlyweight()        
        self.__flyweights['Z'] = ConcreteFlyweight()
    def GetFlyweight(self, key):
        return self.__flyweights[key]

def main():
    extrinsicstate = 22
    ff = FlyweightFactory()
    fwx = ff.GetFlyweight('X')
    fwx.Operation(extrinsicstate)
    fwy = ff.GetFlyweight('Y')
    fwy.Operation(extrinsicstate)
    fwz = ff.GetFlyweight('Z')
    fwz.Operation(extrinsicstate)
    usfw = UnShareConcreteFlyweight()
    usfw.Operation(extrinsicstate)
    
if __name__ == '__main__':
    main()
    
              
