#!/usr/bin/env python
from copy import copy,deepcopy
class WorkExperience:
    @property
    def workDate(self):
        return self.__workDate
    @workDate.setter
    def workDate(self,value):
        self.__workDate = value
    @property
    def Company(self):
        return self.__company
    @Company.setter
    def Company(self, value):
        self.__company = value
    def Clone(self):
        return copy(self)

class Resume:
    def __init__(self,name):
        self.__name = name
        self.__work = WorkExperience()
    def CopyWork(self,work):
        self.__work = work.Clone()
    def SetPersonalInfo(self,sex, age):
        self.__sex = sex
        self.__age = age
    def SetWorkExperience(self, workDate, company):
        self.__work.workDate = workDate
        self.__work.Company = company
    def Display(self):
        print(self.__name,self.__sex,self.__age)
        print(self.__work.workDate, self.__work.Company)
    def Clone(self):
        resume = deepcopy(self)
        resume.name = self.__name
        resume.sex = self.__sex
        resume.age = self.__age
        return resume

    
if __name__ == '__main__':
    resumeA = Resume('大鸟')
    resumeA.SetPersonalInfo('男','29')
    resumeA.SetWorkExperience('1998-2000','XX公司')
    resumeB = resumeA.Clone()
    resumeB.SetWorkExperience('1998-2006','YY公司')
    resumeC = resumeA.Clone()
    resumeC.SetPersonalInfo('男','24')
    resumeC.SetWorkExperience('1998-2003','ZZ公司')
    resumeA.Display()
    resumeB.Display()    
    resumeC.Display()






