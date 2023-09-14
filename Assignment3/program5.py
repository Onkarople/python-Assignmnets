#Addition of prime Number from N Numbers with 2 modules

from MarvellousNum import ChkPrime

def primelist(Data):

    sum=0
    for no in Data:
        if(ChkPrime(no)):
            sum=sum+no

    return sum


def main():
    print("How many elemnts you want to store")
    iSize=int(input())

    Data=list()

    print("Enter Data")

    for i in range(0,iSize,1):
        No=int(input())
        Data.append(No)
    
    Ans=primelist(Data)
    print("Addition of prime numbers is:",Ans)


if __name__=="__main__":
    main()