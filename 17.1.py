#!/usr/bin/env python
from abc import abstractmethod
class Target:
    @abstractmethod
    def Request(self):
        print("normal request")

class Adaptee:
    def SpecificRequest(self):
        print("special request")

class Adapter(Target):
    def __init__(self):
        self.__adaptee = Adaptee()
    def Request(self):
        self.__adaptee.SpecificRequest()

def main():
    target = Adapter()
    target.Request()

if __name__ == '__main__':
    main()
