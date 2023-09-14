#check number positive or negative


from tkinter.tix import Tree


def Chek(No):
    if(No<0):
        return False
    else:
        return True


def main():
    print("Enter number")

    No=int(input())

    Ret=Chek(No)

    if(Ret==True):
        print("positive number")
    else:
        print("negative number")



if __name__=="__main__":
    main()
