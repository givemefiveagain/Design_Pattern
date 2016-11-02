#!/usr/bin/env python
from abc import abstractmethod

class State:
    @abstractmethod
    def WriteProgram(self, work):
        pass

class ForenoonState(State):
    def WriteProgram(self, work):
        if( work.Hour < 12):
            print("current time: ",work.Hour,' work at morning, spirit')
        else:
            work.SetState(NoonState())
            work.WriteProgram()

class NoonState(State):
    def WriteProgram(self, work):
        if( work.Hour < 13):
            print("current time: ",work.Hour,' dinner time, hungery')
        else:
            work.SetState(AfternoonState())
            work.WriteProgram()
        
class AfternoonState(State):
    def WriteProgram(self, work):
        if( work.Hour < 17):
            print("current time: ",work.Hour,' work at afternoon, spirit')
        else:
            work.SetState(EveningState())
            work.WriteProgram()

class EveningState(State):
    def WriteProgram(self, work):
        if( work.TaskFinished):
            work.SetState(ResetState())
            work.WriteProgram()
        else:
            if(work.Hour < 12):
               print("current time: ",work.Hour,' work overtime, very tired')
            else:
                work.SetState(SleepingState())
                work.WriteProgram()
                
class SleepingState(State):
    def WriteProgram(self, work):
        print("current time: ",work.Hour,' canot work anymore, sleep')

class ResetState(State):
    def WriteProgram(self, work):
        print("current time: ",work.Hour,' it is time to go home')

class Work:
    def __init__(self):
        self.current = ForenoonState()
    @property
    def Hour(self):
        return self.__hour
    @Hour.setter
    def Hour(self,value):
        self.__hour = value
    @property
    def TaskFinished(self):
        return self.__finish
    @TaskFinished.setter
    def TaskFinished(self,value):
        self.__finish = value
    def SetState(self, state):
        self.current = state
    def WriteProgram(self):
        self.current.WriteProgram(self)

def main():
    wk = Work()
    wk.Hour = 9
    wk.WriteProgram()
    wk.Hour = 10
    wk.WriteProgram()
    wk.Hour = 12
    wk.WriteProgram()
    wk.Hour = 14
    wk.WriteProgram()
    wk.Hour = 17
    wk.TaskFinished = False
    wk.WriteProgram()
    wk.Hour = 20
    wk.WriteProgram()    
    wk.Hour = 22
    wk.WriteProgram()

if __name__ == '__main__':
    main()

    

        
