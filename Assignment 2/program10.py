#return addition of digits


def count(No):
    sum=0
    while(No!=0):
        digit=No%10
        sum=sum+digit
        No=No//10
    
    return sum


def main():
    print("Enter number")
    No=int(input())

    Ret=count(No)

    print("sum is:",Ret)


if __name__=="__main__":
    main()