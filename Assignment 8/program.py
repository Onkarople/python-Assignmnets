
def Sum(No):
    if(No<=0):
        return 0
    else:
        iDigit=No%10
        return(iDigit+Sum(No=No//10))
       


def main():
    No=int(input("Enter Number : "))
    Ret=Sum(No)
    print("Sumation is :",Ret)

if __name__=="__main__":
    main()