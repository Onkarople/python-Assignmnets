#Filter(),Map(),Reduce()
from functools import reduce


def ChkNum(No):
    return No>=70 and No<=90

def increment(No):
    return No+10

def Mult(A,B):
    return A*B


def Acceptlist():
    print("How many elements you want")
    iSize=int(input())

    Data=list()
    print("Enter data")

    for i in range(0,iSize,1):
        No=int(input())
        Data.append(No)
    
    return Data


def main():
   
    Data=Acceptlist()
    
    print("Data is",Data)

    Data_Filter=list(filter(ChkNum,Data))
    print("Data after filter",Data_Filter)

    Data_map=list(map(increment,Data_Filter))
    print("Data after map",Data_map)

    Ans=reduce(Mult,Data_map)
    print("Product of all numbers is:",Ans)


if __name__ == "__main__":
    main()