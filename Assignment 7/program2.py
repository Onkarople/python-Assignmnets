import threading
import time


def EvenList(Arr):
    sum=0
    for i in Arr:
        if(i%2==0):
            sum=sum+i
    
    print("Sum of even Number is :",sum)
            



def OddList(Arr):
    sum=0
    for i in Arr:
        if(i%2!=0):
            sum=sum+i
    print("Sum of Odd Numbers is : ",sum)


def main():
    Arr=list()

    No=int(input("Hou many elements you have to enter"))

    print("Enter numbers in list")

    for i in range(0,No):
        value=int(input())
        Arr.append(value)
    

    print("list is : ",Arr)

    T1=threading.Thread(target=EvenList,args=(Arr,))
    T2=threading.Thread(target=OddList,args=(Arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__=="__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Excution Time is:",end_time-start_time)