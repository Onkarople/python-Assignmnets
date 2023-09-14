#Find Maximum from N Numbers

def Maximum(Data):
    iMax=0

    for No in Data:
        if(No>iMax):
            iMax=No
    
    return iMax
    

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

    Max=Maximum(Data)
    print("Maximum Element is:",Max)
    
   
    

if __name__=="__main__":
    main()
