#!/usr/bin/env python
from abc import abstractmethod,ABCMeta

class StockObserver:
    def __init__(self,subject, name):
        self.__subject = subject
        self.__name = name
    def CloseStockMarket(self):
        print(self.__subject.SubjectState,self.__name,'close stock, continue working')

class NBAObserver:
    def __init__(self,subject, name):
        self.__subject = subject
        self.__name = name
    def CloseNBADirectSeeding(self):
        print(self.__subject.SubjectState,self.__name,'close stock, continue working')
        
class Subject:
    __metaclass__ = ABCMeta    
    def __init__(self):
        self.__observers = list()
    def Notify(self):
        pass
    @property
    def SubjectState(self):
        return  self.__SubjectState
    @SubjectState.setter
    def SubjectState(self,value):
        self.__SubjectState = value        
            
class Boss(Subject):
    def __init__(self):
        self.__observers = list()
    def Update(self,observer):
        self.__observers.append(observer)
    def Notify(self):
        for obs in self.__observers:
            obs()
    @property
    def SubjectState(self):
        return  self.__SubjectState
    @SubjectState.setter
    def SubjectState(self,value):
        self.__SubjectState = value
        

class Secretary(Subject):
    pass
        
def main():
    bs = Boss()
    lily = StockObserver(bs,'lily')
    lucy = NBAObserver(bs,'lucy')
    bs.Update(lily.CloseStockMarket)
    bs.Update(lucy.CloseNBADirectSeeding)
    bs.SubjectState = 'boss is coming' 
    bs.Notify()

if __name__ == '__main__':
    main()
