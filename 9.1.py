#!/usr/bin/env python

class Resume:
    def __init__(self,name):
        self.__name = name
    def SetPersonInfo(self,sex,age):
        self.__sex = sex
        self.__age = age
    def SetWorkExperience(self,timeArea, company):
        self.__timeArea = timeArea
        self.__company = company
    def Display(self):
        print(self.__name,self.__sex,self.__age)
        print("工作经历:",self.__timeArea,self.__company)

def main1():
    resumeA = Resume("大鸟")
    resumeA.SetPersonInfo('男','29')
    resumeA.SetWorkExperience("1998-2000","xx公司")
    resumeB = Resume("大鸟")
    resumeB.SetPersonInfo('男','29')
    resumeB.SetWorkExperience("1998-2000","xx公司")
    resumeC = Resume("大鸟")
    resumeC.SetPersonInfo('男','29')
    resumeC.SetWorkExperience("1998-2000","xx公司")
    resumeA.Display()
    resumeB.Display()
    resumeC.Display()

def main2():
    resumeA = Resume("大鸟")
    resumeA.SetPersonInfo('男','29')
    resumeA.SetWorkExperience("1998-2000","xx公司")    
    resumeB = resumeA
    resumeB.SetWorkExperience('1998-2006','YY公司')    
    resumeC = resumeA
    resumeC.SetPersonInfo('男','24')    
    resumeA.Display()
    resumeB.Display()
    resumeC.Display()
    
if __name__ == '__main__':
    main1()
    main2()
