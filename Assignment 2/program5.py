#Check prime or not


def prime(No):
    for i in range(2,(No//2)+1):
        if(No%i==0):
    
            break
    
    if(i==(No//2)):
        return True
    else:
        return False

def main():
    print("Enter number")
    No=int(input())

    Ret=prime(No)

    if Ret==True:
        print("its prime number")
    else:
        print("Its not prime number")


if __name__=="__main__":
    main()