#lambda function which accepts one number and return power

Powerx=lambda No:No*No

def main():
    print("Enter one number")
    iNo=int(input())

    Ans=Powerx(iNo)

    print("Power is:",Ans)


if __name__ =="__main__":
    main()