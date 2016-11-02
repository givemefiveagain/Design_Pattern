#!/usr/bin/env python
from abc import ABCMeta,abstractmethod

class User:
    def __init__(self):
        self.__name = None
        self.__id = None
    @property
    def ID(self):
        return self.__id
    @ID.setter
    def ID(self,value):
        self.__id = value
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name = value
        
class IUser:
    __metaclass__ = ABCMeta
    def Insert(self, user):
        pass
    def GetUser(self, user):
        pass
    
class SqlServerUser(IUser):
    def Insert(self,user):
        print('insert one user record in SQL Server',user.Name)
    def GetUser(self,user):
        print('Get one user record from SQL Server',user.ID)

class AccessUser(IUser):
    def Insert(self,user):
        print('insert one user record in Access Server',user.Name)
    def GetUser(self,user):
        print('Get one user record from Access Server',user.ID)

class IFactory:
    def CreateUser(self):
        pass

class SqlServerFactory(IFactory):
    def CreateUser(self):
        return SqlServerUser()

class AccessFactory(IFactory):
    def CreateUser(self):
        return AccessUser()

def main():
    user = User()
    factory = SqlServerFactory()
    iu = factory.CreateUser()
    iu.Insert(user)
    iu.GetUser(user)

if __name__ == '__main__':
    main()
        
