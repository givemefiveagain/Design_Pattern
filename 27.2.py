#!/usr/bin/env python
from abc import ABCMeta, abstractmethod
import re 
class PlayContext:
    @property
    def PlayText(self):
        return self.__text
    @PlayText.setter
    def PlayText(self,value):
        self.__text = value

class Expression:
    __metaclass__ = ABCMeta
    def Interpret(self, context):
        if len(context.PlayText) == 0:
            return
        else:            
            playkey = context.PlayText[0]
            context.playText = context.PlayText[2:]
            index = context.playText.find(' ')
            playValue = context.PlayText[index+1]
            context.PlayText = context.PlayText[index+3:]
            #print('index',index)
            #print('PlayText',context.PlayText)
            self.Excute(playkey,playValue)
    @abstractmethod
    def Excute(self, key, value):
        pass

class Note(Expression):
    def Excute(self, key, value):
        notes = {'C':'1','D':'2','E':'3','F':'4',
                 'G':'9','A':'6','B':'7'}
        print(notes[key])

class Scale(Expression):
    def Excute(self, key, value):
        scales = {'1':'低音','2':'中音','3':'高音'}
        print(scales[value])

def main():
    context = PlayContext()
    print('上海滩')
    context.PlayText='O 2 E 0.5 G 0.5 A 3 E 0.5 G 0.5 D 3 E 0.5 G 0.5 A 0.5 O 1'
    while(len(context.PlayText) > 3):
        strs = context.PlayText[0]
        if strs in ['O']:
            expression = Scale()
        elif (strs in ['C','D','E','F','G','A','B','P']):
            expression = Note()
        expression.Interpret(context)

if __name__ == '__main__':
    main()
                  
            
            
            
            
            
