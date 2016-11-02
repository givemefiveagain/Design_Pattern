#!/usr/bin/env python
from abc import abstractmethod,ABCMeta

class Subject:
    __metaclass__ = ABCMeta    
    def __init__(self):
        self.__observers = list()
    def Attach(self,observer):
        self.__observers.append(observer)
    def Detach(self,observer):
        self.__observers.pop(observer)    
    def Notify(self):
        for observer in self.__observers:
            observer.Update()
            
class ConcreteSubject(Subject):
    def __init__(self):
        super(ConcreteSubject,self).__init__()
        self.__SubjectState = None
    @property
    def SubjectState(self):
        return  self.__SubjectState
    @SubjectState.setter
    def SubjectState(self,value):
        self.__SubjectState = value
    
class Observer:
    __metaclass__=ABCMeta
    @abstractmethod
    def Update(self):
        pass
    
class ConcreteObserver(Observer):
    def __init__(self,subject, name):
        self.__subject = subject
        self.__name = name
    def Update(self):
        self.__observerState = self.__subject.SubjectState
        print('the new state of observer ',self.__name,self.__observerState)
    @property
    def Subject(self):
        return self.__subject
    @Subject.setter
    def Subject(self,value):
        self.__subject = value
        
def main():
    cs = ConcreteSubject()
    lily = ConcreteObserver(cs,'lily')
    lucy = ConcreteObserver(cs,'lucy')
    jack = ConcreteObserver(cs,'jack')
    cs.Attach(lily)
    cs.Attach(lucy)
    cs.Attach(jack)
    cs.SubjectState = 'ABC'
    cs.Notify()

if __name__ == '__main__':
    main()
