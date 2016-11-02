#!/usr/bin/env python

class SubSystemOne:
    def MethodOne(self):
        print("SubSystem One, Method One")

class SubSystemTwo:
    def MethodTwo(self):
        print("SubSystem Two, Method Two")

class SubSystemThree:
    def MethodThree(self):
        print("SubSystem Three, Method Three")

class SubSystemFour:
    def MethodFour(self):
        print("SubSystem Four, Method Four")

class Facade:
    def __init__(self):
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()
    def MethodA(self):
        print("Method A ----")
        self.one.MethodOne()
        self.two.MethodTwo()
        self.four.MethodFour()
    def MethodB(self):
        print("Method B ----")
        self.two.MethodTwo()
        self.three.MethodThree()

def main():
    facade = Facade()
    facade.MethodA()
    facade.MethodB()

if __name__ == '__main__':
    main()
