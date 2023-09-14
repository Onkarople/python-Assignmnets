#Factorial output


def Fact(No):
    Ans=1
    while(No!=0):
        Ans=Ans*No
        No=No-1
    
    return Ans


def main():
    print("Enter number")
    No=int(input())
    Ret=Fact(No)
    print("Factorial is:",Ret)



if __name__=="__main__":
    main()
