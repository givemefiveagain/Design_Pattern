#!/usr/bin/env python
from abc import abstractmethod,ABCMeta

class Handler:
    __metaclass__ = ABCMeta
    def SetSuccessor(self, successor):
        self._successor = successor
    @abstractmethod
    def HandleRequest(self, request):
        pass

class ConcreteHandler1(Handler):
    def HandleRequest(self, request):
        if request >= 0 and request <= 10:
            print(self.__class__.__name__, 'handle request ', request)
        elif self._successor != None:
            self._successor.HandleRequest(request)

class ConcreteHandler2(Handler):
    def HandleRequest(self, request):
        if request >= 10 and request <= 20:
            print(self.__class__.__name__, 'handle request ', request)
        elif self._successor != None:
            self._successor.HandleRequest(request)

class ConcreteHandler3(Handler):
    def HandleRequest(self, request):
        if request >= 20 and request <= 30:
            print(self.__class__.__name__, 'handle request ', request)
        elif self._successor != None:
            self._successor.HandleRequest(request)

def main():
    ch1 = ConcreteHandler1()
    ch2 = ConcreteHandler2()
    ch3 = ConcreteHandler3()
    ch1.SetSuccessor(ch2)
    ch2.SetSuccessor(ch3)
    request = [2,5,14,22,18,3,27,20]
    for rt in request:
        ch1.HandleRequest(rt)

if __name__ == '__main__':
    main()
