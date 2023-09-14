#prime numbers 
from functools import reduce


def Checkprime(No):
    i=0
    if(No==2):
        return No
        
    for i in range(2,No,1):
        if(No%i==0):
            break
    
    if i==No-1:
       return No


def Powerx(No):
    return No*2


def reducex(Data):
    iMax=0
    for No in Data:
        if(No>iMax):
            iMax=No
    
    return iMax

    



def AcceptList():
    Data_Input=list()

    print("how many number you want")
    iSize=int(input())

    print("enter Numbers")

    for iCnt in range(0,iSize,1):
        Value=int(input())
        Data_Input.append(Value)

    return Data_Input


def main():
    
    Data_Input=AcceptList() 
    print("List is",Data_Input)

    Arr_Filter=list(filter(Checkprime,Data_Input))
    print("Data after filter",Arr_Filter)

    Arr_map=list(map(Powerx,Arr_Filter))
    print("data after map",Arr_map)

    Ret=reducex(Arr_map)
    print("data after reduce",Ret)


if __name__ =="__main__":
    main()