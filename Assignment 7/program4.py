import threading
import time


def small(Str):
    Cnt=0
    for char in range(len(Str)):
        if(Str[char]>='a' and Str[char]<='z'):
            Cnt=Cnt+1
    
    print("Count of small charcters is :",Cnt)



def Capital(Str):
    Cnt=0
    for char in range(len(Str)):
        if(Str[char]>='A' and Str[char]<='Z'):
            Cnt=Cnt+1
    
    print("Count of Capital charcters is :",Cnt)


def Digit(Str):
    Cnt=0
    for char in range(len(Str)):
        if(Str[char]>= '1' and Str[char]<='9'):
            Cnt=Cnt+1
    
    print("Count of Digits charcters is :",Cnt)






def main():
    Str=input("Enter String : ")

    T1=threading.Thread(target=small,args=(Str,))
    T2=threading.Thread(target=Capital,args=(Str,))
    T3=threading.Thread(target=Digit,args=(Str,))

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()




if __name__ == "__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Excution Time is:",end_time-start_time)