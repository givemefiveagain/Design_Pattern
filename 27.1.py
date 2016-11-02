#!/usr/bin/env python
from abc import abstractmethod,ABCMeta
class AbstractExpression:
    __metaclass__ = ABCMeta
    @abstractmethod
    def Interpret(self, context):
        pass

class TerminalExpression(AbstractExpression):
    def Interpret(self, context):
        print("termianl interpretor")

class NonterminalExpression(AbstractExpression):
    def Interpret(self, context):
        print("Nontermianl interpretor")

class Context:
    @property
    def Input(self):
        return self.__input
    @Input.setter
    def Input(self,value):
        self.__input = value
    @property
    def Output(self):
        return self.__output
    @Output.setter
    def Output(self,value):
        self.__output = value
        
def main():
    ct = Context()
    lt = list()
    lt.append(TerminalExpression())
    lt.append(NonterminalExpression())
    lt.append(TerminalExpression())              
    lt.append(TerminalExpression())
    for ae in lt:
        ae.Interpret(ct)

if __name__ == '__main__':
    main()
