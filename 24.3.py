#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Request:
    @property
    def RequestType(self):
        return self.__requestType
    @RequestType.setter
    def RequestType(self,value):
        self.__requestType = value
    @property
    def RequestContent(self):
        return self.__requestContent
    @RequestContent.setter
    def RequestContent(self,value):
        self.__requestContent = value
    @property
    def Number(self):
        return self.__number
    @Number.setter
    def Number(self,value):
        self.__number = value

class Manager:
    __metaclass__ = ABCMeta
    def __init__(self, name):
        self._name = name
    def SetSuperior(self, superior):
        self._superior = superior
    @abstractmethod
    def RequestApplications(self, request):
        pass

class CommonManager(Manager):
    def __init__(self,name):
        super(CommonManager,self).__init__(name)
    def RequestApplications(self, request):
        if request.RequestType == 'leave' and request.Number <= 2:
            print(self.__class__.__name__,':', request.RequestContent,'number',request.Number,'is approved')
        else:
            if self._superior != None:
                self._superior.RequestApplications(request)

class Majordomo(Manager):
    def __init__(self,name):
        super(Majordomo,self).__init__(name)
    def RequestApplications(self, request):
        if request.RequestType == 'leave' and request.Number <= 5:
            print(self.__class__.__name__,':', request.RequestContent,'number',request.Number,'is approved')
        else:
            if self._superior != None:
                self._superior.RequestApplications(request)

class GeneralManager(Manager):
    def __init__(self,name):
        super(GeneralManager,self).__init__(name)
    def RequestApplications(self, request):
        if request.RequestType == 'leave':
            print(self.__class__.__name__,':', request.RequestContent,'number',request.Number,'is approved')
        elif(request.RequestType == 'salary raise') :
            if (request.Number <= 500):
                print(self.__class__.__name__, request.RequestContent,'Number',request.Number,' is approved')
            else:
                print(self.__class__.__name__, request.RequestContent,'Number',request.Number,' is a little hard, let us talk about it later' )

def main():
    cm = CommonManager('Lily')
    md = Majordomo('Tom')
    gm = GeneralManager('Jack')
    cm.SetSuperior(md)
    md.SetSuperior(gm)
    rt = Request()
    rt.RequestType = 'salary raise'
    rt.RequestContent = 'freshman apply for a salary raise'
    rt.Number = 1000
    cm.RequestApplications(rt)
    rt2 = Request()
    rt2.RequestType = 'leave'
    rt2.RequestContent = 'freshman apply for a annual leave'
    rt2.Number = 3
    cm.RequestApplications(rt2)

if __name__ == '__main__':
    main()
