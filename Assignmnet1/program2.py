#Even and Odd number

def ChkNum(No):
    if(((No%2)==0)):
        return True
    else:
        return False




def main():
    print("Enter number")
    No=int(input())
    Ret=ChkNum(No)
    if(Ret==True):
        print("Even number")
    else:
        print("Odd number")


if __name__ =="__main__":
    main()