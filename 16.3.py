#!/usr/bin/env python
from abc import abstractmethod
class State:
    @abstractmethod
    def Handle(self,context):
        pass

class ConcreteStateA(State):
    def Handle(self,context):
        context.State = ConcreteStateB()

class ConcreteStateB(State):
    def Handle(self,context):
        context.State = ConcreteStateA()

class Context:
    def __init__(self, state):
        self.__state = state
    @property
    def State(self):
        return self.__state
    @State.setter
    def State(self,value):
        self.__state = value
        print("current state is ")
    def Request(self):
        self.__state.Handle(self)

def main():
    ct = Context(ConcreteStateA())
    ct.Request()
    ct.Request()
    ct.Request()
    ct.Request()

if __name__ == '__main__':
    main()
