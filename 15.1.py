#!/usr/bin/env python

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
    
class SqlServerUser:
    def Insert(self,user):
        print('insert one user record in SQL Server',user.Name)
    def GetUser(self,user):
        print('Get one user record from SQL Server',user.ID)

def main():
    user = User()
    ssu = SqlServerUser()
    ssu.Insert(user)
    ssu.GetUser(user)

if __name__ == '__main__':
    main()
        
