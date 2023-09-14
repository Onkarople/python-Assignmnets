#Addition of N Numbers

def Addition(Data):
    Sum=0
    for No in Data:
        Sum=Sum+No
    
    return Sum

def AcceptList():
    print("How many elemnts you want to store")
    iSize=int(input())

    Data=list()

    print("Enter Data")

    for i in range(0,iSize,1):
        No=int(input())
        Data.append(No)
    
    return Data


def main():

    Data=AcceptList()
    print("Data is:",Data)
    
    Ans=Addition(Data)
    print("Addition is",Ans)
    

if __name__=="__main__":
    main()
