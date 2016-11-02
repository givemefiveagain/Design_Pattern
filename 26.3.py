#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
class WebSite:
    __metaclass__ = ABCMeta
    def Use(self):
        pass

class ConcreteWebSite(WebSite):
    def __init__(self, name):
        self.__name = name
    def Use(self):
        print('website classify:',self.__name)

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
    fx.Use()
    fy = wsf.GetWebSiteCategory('Y')
    fy.Use()    
    fps = wsf.GetWebSiteCategory('product show')
    fps.Use()
    fb = wsf.GetWebSiteCategory('blog')
    fb.Use()
    print('the total number of website is',wsf.GetWebSiteCount())
            
if __name__ == '__main__':
    main()
