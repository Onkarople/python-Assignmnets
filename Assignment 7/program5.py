import threading
import time


def Display(No):
    for i in range(1,No+1):
        print("Display 1 To 50 : ",i)


def Reverse(No):
    for i in range(50,0,-1):
        print("Display 1 to 50 in Rverse :",i)



def main():
    Number=50

    T1=threading.Thread(target=Display,args=(Number,))
    T2=threading.Thread(target=Reverse,args=(Number,))

    T1.start()
    T1.join()

    T2.start()
    T2.join()


if __name__ == "__main__":
    start_time=time.process_time()
    main()
    end_time=time.process_time()
    print("Excution Time is:",end_time-start_time)