#!/usr/bin/env python
from abc import abstractmethod

class Player:
    def __init__(self,name):
        self._name = name
    @abstractmethod
    def Attack(self):
        pass
    @abstractmethod
    def Defense(self):
        pass

class Forwards(Player):
    def __init__(self, name):
        super(Forwards,self).__init__(name)
    def Attack(self):
        print("前锋",self._name,"进攻")
    def Defense(self):
        print("前锋",self._name,"防守")

class Center(Player):
    def __init__(self, name):
        super(Center,self).__init__(name)
    def Attack(self):
        print("中锋",self._name,"进攻")
    def Defense(self):
        print("中锋",self._name,"防守")
        
class Guards(Player):
    def __init__(self, name):
        super(Guards,self).__init__(name)
    def Attack(self):
        print("后卫",self._name,"进攻")
    def Defense(self):
        print("后卫",self._name,"防守")
        
class ForeignCenter(Player):
    @property
    def Name(self):
        return self._name
    @Name.setter
    def Name(self, name):
        self._name = name
    def Attack(self):
        print("外籍中锋",self._name,"进攻")
    def Defense(self):
        print("外籍中锋",self._name,"防守")


class Translator(Player):
    def __init__(self,name):
        super(Translator,self).__init__(name)
        self.__fc = ForeignCenter(name)
        self.__fc.Name = name
    def Attack(self):
        self.__fc.Attack()
    def Defense(self):
        self.__fc.Defense()

def main():
    Tom = Forwards('Tom')
    Tom.Attack()
    Joe = Guards('Joe')
    Joe.Attack()
    Fred = Translator('Fred')
    Fred.Attack()
    Fred.Defense()    
        
if __name__ == '__main__':
    main()
