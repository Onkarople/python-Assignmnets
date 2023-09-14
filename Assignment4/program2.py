#lambda function which accepts two paramters and return multiplication

Multix=lambda No1,No2:No1*No2

def main():
    print("Enter first number")
    iNo1=int(input())

    print("Enter second number")
    iNo2=int(input())

    

    Ans=Multix(iNo1,iNo2)

    print("multiplication is:",Ans)


if __name__ =="__main__":
    main()