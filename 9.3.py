#!/usr/bin/env python
from copy import copy

class Resume:
    def __init__(self,name):
        self.__name = name
    def SetPersonalInfo(self, sex, age):
        self.__sex = sex
        self.__age = age
    def SetWorkExperience(self, timeArea, company):
        self.__timeArea = timeArea
        self.__company = company
    def Display(self):
        print(self.__name, self.__sex, self.__age)
        print("工作经历:",self.__timeArea, self.__company)
    def Clone(self):
        return copy(self)

if __name__ == '__main__':
    resumeA = Resume('大鸟')
    resumeA.SetPersonalInfo('男','29')
    resumeA.SetWorkExperience('1998-2000','XX公司')
    resumeB = resumeA.Clone()
    resumeB.SetWorkExperience('1998-2006','YY公司')
    resumeC = resumeA.Clone()
    resumeC.SetPersonalInfo('男','24')
    resumeC.SetWorkExperience('1998-2005','ZZ公司')    
    resumeA.Display()
    resumeB.Display()    
    resumeC.Display()
