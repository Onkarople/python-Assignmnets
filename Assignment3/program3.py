#Find Minimum from N Numbers

def Minimum(Data):
    iMin=Data[0]

    for No in Data:
        if(No<iMin):
            iMin=No
    
    return iMin
    

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

    Min=Minimum(Data)
    print("Minimum Element is:",Min)
    
   
    

if __name__=="__main__":
    main()
