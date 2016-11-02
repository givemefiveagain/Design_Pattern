#!/usr/bin/env python

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
    def __init__(self,name):
        self._name = name
    def GetResult(self, managerLevel, request):
        if(managerLevel == 'manager'):
            if ((request.RequestType == 'leave') and (request.Number <= 2)) :
                print(self._name, request.RequestContent,'Number',request.Number,' is approved')
            else:
                print(self._name, request.RequestContent,'Number',request.Number,' is not approved, is not my authority')
        elif(managerLevel == 'director'):
            if ((request.RequestType == 'leave') and (request.Number <= 5)) :
                print(self._name, request.RequestContent,'Number',request.Number,' is approved')
            else:
                print(self._name, request.RequestContent,'Number',request.Number,' is not approved, is not my authority')
        elif(managerLevel == 'general manager'):
            if (request.RequestType == 'leave') :
                print(self._name, request.RequestContent,'Number',request.Number,' is approved')
            elif (request.RequestType == 'salary raise') :
                if (request.Number <= 500):
                    print(self._name, request.RequestContent,'Number',request.Number,' is approved')
                else:
                    print(self._name, request.RequestContent,'Number',request.Number,' is a little hard, let us talk about it later' )

def main():
    mr1 = Manager('Lily')
    mr2 = Manager('Tom')
    mr3 = Manager('Jack')
    rt = Request()
    rt.RequestType = 'salary raise'
    rt.RequestContent = 'freshman apply for a salary raise'
    rt.Number = 1000
    mr1.GetResult('manager',rt)
    mr2.GetResult('director',rt)
    mr3.GetResult('general manager', rt)
    rt2 = Request()
    rt2.RequestType = 'leave'
    rt2.RequestContent = 'freshman apply for a annual leave'
    rt2.Number = 3
    mr1.GetResult('manager',rt2)
    mr2.GetResult('director',rt2)
    mr3.GetResult('general manager', rt2)    

if __name__ == '__main__':
    main()
    


                    
