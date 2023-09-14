#Find Frequency of one number from N Numbers

def Frequency(Data,iNo):
    iCnt=0

    for No in Data:
        if(iNo==No):
         iCnt=iCnt+1
    
    return iCnt
    

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

    print("Enter one Number")
    iNo=int(input())

    iFre=Frequency(Data,iNo)
    print("Frequency of {} is".format(iNo),iFre)

   
    

if __name__=="__main__":
    main()
