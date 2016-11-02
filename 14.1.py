#!/usr/bin/env python

class Secretary:
    def __init__(self):
        self.action = None
        self.observers = list()
    def Attach(self,observer):
        self.observers.append(observer)
    def Notify(self):
        for observer in self.observers:
            observer.Update()
    @property
    def SecretaryAction(self):
        return self.action
    @SecretaryAction.setter
    def SecretaryAction(self,value):
        self.action = value

class StockObserver:
    def __init__(self,name,sub):
        self.__name = name
        self.__sub = sub
    def Update(self):
        print(self.__sub.SecretaryAction,self.__name,"close stock, continue working")

def main():
    meimei = Secretary()
    so1 = StockObserver('lucy',meimei)
    so2 = StockObserver('lily',meimei)
    meimei.Attach(so1)
    meimei.Attach(so2)
    meimei.SecretaryAction = 'Boss is coming'
    meimei.Notify()

if __name__ == '__main__':
    main()
    
