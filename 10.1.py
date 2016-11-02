#!/usr/bin/env python

class TestPaperA:
    def TestQuestion1(self):
        print('TestQuestion1')
        print('Answer: b')
    def TestQuestion2(self):
        print('TestQuestion2')
        print('Answer: a')
    def TestQuestion3(self):
        print('TestQuestion3')
        print('Answer: c')

class TestPaperB:
    def TestQuestion1(self):
        print('TestQuestion1')
        print('Answer: d')
    def TestQuestion2(self):
        print('TestQuestion2')
        print('Answer: b')
    def TestQuestion3(self):
        print('TestQuestion3')
        print('Answer: a')

def main():
    print("Student A's Test paper")
    studentA = TestPaperA()
    studentA.TestQuestion1()
    studentA.TestQuestion2()
    studentA.TestQuestion3()
    print("Student B's Test paper")
    studentB = TestPaperB()
    studentB.TestQuestion1()
    studentB.TestQuestion2()
    studentB.TestQuestion3()

if __name__ == '__main__':
    main()
