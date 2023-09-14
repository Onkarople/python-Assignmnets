#Additon of factors



def Factors(No):
    sum=0
    for i in range(1,No):
        if(No%i==0):
            sum=sum+i
    

    return sum


def main():
    print("Enter number")
    No=int(input())

    Ret=Factors(No)
    print("Addition of factors is:",Ret)


if __name__ =="__main__":
    main()