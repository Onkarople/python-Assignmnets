#Count number of digits


def count(No):
    iCnt=0
    while(No!=0):
        iCnt=iCnt+1
        No=No//10
    
    return iCnt


def main():
    print("Enter number")
    No=int(input())

    Ret=count(No)

    print("Count is:",Ret)


if __name__=="__main__":
    main()