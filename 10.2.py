#!/usr/bin/env python
from abc import ABCMeta,abstractmethod
class TestPaper:
    __metaclass__ = ABCMeta
    def TestQuestion1(self):
        print('TestQuestion1')
        print('Answer:',self._Answer1())
    @abstractmethod
    def _Answer1(self):
        pass        

class TestPaperA(TestPaper):
    def _Answer1(self):
        return 'b'

class TestPaperB(TestPaper):
    def _Answer1(self):
        return 'c'

def main():
    print("Student A's Test paper")
    studentA = TestPaperA()
    studentA.TestQuestion1()
    print("Student B's Test paper")
    studentB = TestPaperB()
    studentB.TestQuestion1()

if __name__ == '__main__':
    main()
