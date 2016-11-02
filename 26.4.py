#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
class User:
    def __init__(self,name):
        self.__name = name
    @property
    def Name(self):
        return self.__name

class WebSite:
    __metaclass__ = ABCMeta
    @abstractmethod
    def Use(self, use):
        pass

class ConcreteWebSite(WebSite):
    def __init__(self, name):
        self.__name = name
    def Use(self, user):
        print("website classify :",self.__name,"user: ",user.Name)

class WebSiteFactory:
    def __init__(self):
        self.__flyweights = dict()
    def GetWebSiteCategory(self, key):
        if(key not in self.__flyweights):
            self.__flyweights[key] = ConcreteWebSite(key)
        return self.__flyweights[key]
    def GetWebSiteCount(self):
        return len(self.__flyweights)

def main():
    wsf = WebSiteFactory()
    fx = wsf.GetWebSiteCategory('X')
    fx.Use(User('freshman'))
    fy = wsf.GetWebSiteCategory('Y')
    fy.Use(User('BigBird'))    
    fps = wsf.GetWebSiteCategory('product show')
    fps.Use(User('Lily'))
    fb = wsf.GetWebSiteCategory('blog')
    fb.Use(User('Lucy'))
    print('the total number of website is',wsf.GetWebSiteCount())
            
if __name__ == '__main__':
    main()
