#!/usr/bin/env python
from abc import ABCMeta, abstractmethod

class Strategy:
    __metaclass__ = ABCMeta
    @abstractmethod
    def AlgorithmInterface(self):
        pass

class ConcreteStrategyA(Strategy):
    def AlgorithmInterface(self):
        print("算法A的实现")

class ConcreteStrategyB(Strategy):
    def AlgorithmInterface(self):
        print("算法B的实现")

class ConcreteStrategyC(Strategy):
    def AlgorithmInterface(self):
        print("算法C的实现")

class Context:
    def __init__(self, strategy):
        self.strategy = strategy
    def ContextInterface(self):
        self.strategy.AlgorithmInterface()

if __name__ == '__main__':
    context = Context(ConcreteStrategyA())
    context.ContextInterface()
    context = Context(ConcreteStrategyB())
    context.ContextInterface()
    context = Context(ConcreteStrategyC())
    context.ContextInterface()
    
    
