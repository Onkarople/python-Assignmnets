#number is divisible by 5 or not

def ChkNum(No):
    if(((No%5)==0)):
        return True
    else:
        return False




def main():
    print("Enter number")
    No=int(input())
    Ret=ChkNum(No)
    if(Ret==True):
        print("True")
    else:
        print("False")


if __name__ =="__main__":
    main()