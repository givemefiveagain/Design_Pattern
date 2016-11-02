#!/usr/bin/env python

class work:
    @property
    def Hour(self):
        return self.__hour
    @Hour.setter
    def Hour(self,value):
        self.__hour = value
    @property
    def TaskFinished(self):
        self.__finish = False
    @TaskFinished.setter
    def TaskFinished(self,value):
        self.__finish = value
    def WriteProgram(self):
        if(self.__hour < 12):
            print("current time: ",self.__hour,' work at morning, spirit')
        elif(self.__hour < 13):
            print("current time: ",self.__hour,' work at noon, sleepy')
        elif(self.__hour < 17):
            print("current time: ",self.__hour,'work at afternoon, spirit')        
        else:
            if(self.__finish ):
                print("current time: ",self.__hour,' leave out of office.')
            else:
                if(self.__hour < 21):
                    print("current time: ",self.__hour,' work overtime, very tired')
                else:
                    print("current time: ",self.__hour,' canot work anymore, sleep')
                
def main():
    wk = work()
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
    
