#Function ADD,SUB,MULT,DIV

def ADD(No1,No2):
    Ans=No1+No2

    return Ans



def SUB(No1,No2):
    Ans=No1-No2

    return Ans



def MUL(No1,No2):
    Ans=No1*No2

    return Ans




def DIV(No1,No2):
    Ans=No1/No2

    return Ans








def main():
    print("Enter first number")
    No1=int(input())

    print("Enter second number")
    No2=int(input())

    Ret=ADD(No1,No2)
    print("Addition is:",Ret)

    
    Ret=SUB(No1,No2)
    print("substraction is:",Ret)

    
    Ret=MUL(No1,No2)
    print("multiplication is:",Ret)

    
    Ret=DIV(No1,No2)
    print("division is:",Ret)



if __name__ =="__main__":
    main()

