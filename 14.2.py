#!/usr/bin/env python
from abc import abstractmethod
class Observer:
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
        print(self._sub.SecretaryAction,self._name,"close stock, continue working")

class NBAObserver(Observer):
    def __init__(self,name,sub):
        super(NBAObserver,self).__init__(name,sub)
    def Update(self):
        print(self._sub.SecretaryAction,self._name,"close NBA, continue working")

class Secretary:
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
    @property
    def SecretaryAction(self):
        return self.action
    @SecretaryAction.setter
    def SecretaryAction(self,value):
        self.action = value

def main():
    meimei = Secretary()
    so1 = StockObserver('lucy',meimei)
    ns1 = NBAObserver('lily',meimei)
    meimei.Attach(so1)
    meimei.Attach(ns1)
    meimei.SecretaryAction = 'Boss is coming'
    meimei.Notify()

if __name__ == '__main__':
    main()
