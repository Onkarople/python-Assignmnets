import threading
import time


def DisplayEven(No):
    for i in range(1,No+1):
        if(i%2==0):
            print("Even Number : ",i)



def DisplayOdd(No):
    for i in range(1,No+1):
        if(i%2!=0):
            print("Odd Number : ",i)


def main():
    No=int(input("Enter Number : "))

    T1=threading.Thread(target=DisplayEven,args=(No,))
    T2=threading.Thread(target=DisplayOdd,args=(No,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Excution Time is :",end_time-start_time)