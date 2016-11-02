#!/usr/bin/env python

class Proxy:
    def __init__(self, girl):
        self.girl = girl
    def GiveDolls(self):
        print(self.girl.name,",give you a doll")
    def GiveFlowers(self):
        print(self.girl.name,",give you flowers")
    def GiveChocolate(self):
        print(self.girl.name,",give you chocolate")

class Girl:
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

def main():
    lily = Girl()
    lily.name = 'lily'
    tom = Proxy(lily)
    tom.GiveDolls()
    tom.GiveFlowers()
    tom.GiveChocolate()
    
if __name__ == '__main__':
    main()
