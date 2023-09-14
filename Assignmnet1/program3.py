#Addition of two numbers

def Add(No1,No2):
    Ans=No1+No2
    return Ans

def main():
    print("Enter first number")
    No1=input()

    print("Enter second number")
    No2=input()

    Ret=Add(int(No1),int(No2))

    print("Addition is :",Ret)



if __name__ =="__main__":
    main()