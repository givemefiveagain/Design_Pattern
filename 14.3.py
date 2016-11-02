#!/usr/bin/env python
from abc import abstractmethod,ABCMeta
class Subject:
    __metaclass__ = ABCMeta
    def Attach(self,observer):
        pass
    def Detach(self,observer):
        pass
    def Notify(self):
        pass
    @property
    def SubjectState(self):
        pass
    @SubjectState.setter
    def SubjectState(self,value):
        pass

class Boss(Subject):
    def __init__(self):
        self.__action = None
        self.__observers = list()
    def Attach(self,observer):
        self.__observers.append(observer)
    def Detach(self,observer):
        self.__observers.pop(observer)    
    def Notify(self):
        for observer in self.__observers:
            observer.Update()
    def SubjectState(self):
        return self.__action    
    def SubjectState(self,value):
        self.__action = value

class Secretary(Subject):
    def __init__(self):
        self.__action = None
        self.__observers = list()
    def Attach(self,observer):
        self.__observers.append(observer)
    def Detach(self,observer):
        self.__observers.pop(observer)    
    def Notify(self):
        for observer in self.__observers:
            observer.Update()
    def SubjectState(self):
        return self.__action    
    def SubjectState(self,value):
        self.__action = value

class Observer:
    __metaclass__=ABCMeta
    def __init__(self,name,sub):
        self._name = name
        self._sub = sub
    @abstractmethod
    def Update(self):
        pass

class StockObserver(Observer):
    def __init__(self,name,sub):
        super(StockObserver,self).__init__(name,sub)
    def Update(self):
        print(self._sub.SubjectState,self._name,"close stock, continue working")

class NBAObserver(Observer):
    def __init__(self,name,sub):
        super(NBAObserver,self).__init__(name,sub)
    def Update(self):
        print(self._sub.SubjectState,self._name,"close NBA, continue working")

def main():
    bs = Boss()
    so1 = StockObserver('lucy',bs)
    ns1 = NBAObserver('lily',bs)
    bs.Attach(so1)
    bs.Attach(ns1)
    bs.SubjectState = 'Boss is coming'
    bs.Notify()

if __name__ == '__main__':
    main()
