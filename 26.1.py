#!/usr/bin/env python

class WebSite:
    def __init__(self, name):
        self.__name = name
    def Use(self):
        print('classify website:',self.__name)

def main():
    ps = WebSite('Product Show')
    ps.Use()
    ps2 = WebSite('Product Show')
    ps2.Use()
    ps3 = WebSite('Product Show')
    ps3.Use()
    ps4 = WebSite('blog Show')
    ps4.Use()
    
if __name__ == '__main__':
    main()
