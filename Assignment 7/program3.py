import threading
import time


def EvenFactor(No):
    sum=0
    value=0
    for i in range(1,No+1):
        if(i%2==0):
            value=i
            for i in range(1,value+1):
                if(value%i==0):
                    sum=sum+i
    
    print("Sum of even factor after Considering Number Itself as a Factor is : ",sum)



def OddFactor(No):
    sum=0
    value=0
    for i in range(1,No+1):
        if(i%2!=0):
            value=i
            for i in range(1,value+1):
                if(value%i==0):
                    sum=sum+i
    
    print("Sum of odd factor after Considering Number Itself as a Factor is : ",sum)





def main():
    No=int(input("Enter Number : "))

    T1=threading.Thread(target=EvenFactor,args=(No,))
    T2=threading.Thread(target=OddFactor,args=(No,))
   

    T1.start()
    T2.start()
   

    T1.join()
    T2.join()

    print("End main")
  


if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Excution Time is:",end_time-start_time)