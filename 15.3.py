#!/usr/bin/env python
from abc import ABCMeta,abstractmethod

class Department:
    def __init__(self):
        self.__id = None
        self.__name = None
    @property
    def DeptName(self):
        return self.__name
    @DeptName.setter
    def DeptName(self,value):
        self.__name = value
    @property
    def ID(self):
        return self.__id
    @ID.setter
    def ID(self,value):
        self.__id = value

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
    @abstractmethod
    def Insert(self, user):
        pass
    @abstractmethod
    def GetUser(self, user):
        pass
    
class SqlServerUser(IUser):
    def Insert(self,user):
        print('insert one user record in SQL Server',user.Name)
    def GetUser(self,user):
        print('Get one user record from SQL Server',user.ID)

class AccessServerUser(IUser):
    def Insert(self,user):
        print('insert one user record in Access Server',user.Name)
    def GetUser(self,user):
        print('Get one user record from Access Server',user.ID)
        
class IDepartment:
    @abstractmethod
    def Insert(self,department):
        pass
    @abstractmethod
    def GetDepartment(self, department):
        pass

class SqlServerDepartment(IDepartment):
    def Insert(self,department):
        print('insert one user record in SQL Server',department.Name)
    def GetUser(self,department):
        print('Get one user record from SQL Server',department.ID)
        
class AccessServerDepartment(IDepartment):
    def Insert(self,department):
        print('insert one user record in Access Server',department.DeptName)
    def GetUser(self,department):
        print('Get one user record from Access Server',department.ID)

class IFactory:
    @abstractmethod
    def CreateUser(self):
        pass
    @abstractmethod
    def CreateDepartment(self):
        pass

class SqlServerFactory(IFactory):
    def CreateUser(self):
        return SqlServerUser()
    def CreateDepartment(self):
        return SqlServerDepartment()

class AccessServerFactory(IFactory):
    def CreateUser(self):
        return AccessServerUser()
    def CreateDepartment(self):
        return AccessServerDepartment()

def main():
    user = User()
    dept = Department()
    factory = AccessServerFactory()
    iu = factory.CreateUser()
    iu.Insert(user)
    iu.GetUser(user)

    cds = factory.CreateDepartment()
    cds.Insert(dept)
    cds.GetUser(dept)

if __name__ == '__main__':
    main()
    
