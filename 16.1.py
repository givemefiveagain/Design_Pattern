#!/usr/bin/env python

def WriteProgram(hour, workFinished=False):
    if(hour < 12):
        print("current time: ",hour,' work at morning, spirit')
    elif(hour < 13):
        print("current time: ",hour,' work at noon, sleepy')
    elif(hour < 17):
        print("current time: ",hour,' work at afternoon, spirit')
    else:
        if(workFinished):
            print("current time: ",hour,' leave out of office.')
        else:
            if(hour < 21):
                print("current time: ",hour,' work overtime, very tired')
            else:
                print("current time: ",hour,' canot work anymore, sleep')
   
def main():
    hour = 9
    WriteProgram(hour)
    hour = 10
    WriteProgram(hour)    
    hour = 12
    WriteProgram(hour)                
    hour = 14
    WriteProgram(hour)        
    hour = 16
    WriteProgram(hour)        
    hour = 18
    WriteProgram(hour)        
    hour = 21
    WriteProgram(hour)    

if __name__ == '__main__':
    main()
