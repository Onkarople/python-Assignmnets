#Object oriented apporch/concept
class Arthematic:
    def __init__(self):
        self.Value1=0
        self.Value2=0
    
    def Accept(self):
        print("Enter First Number")
        self.Value1=int(input())

        print("Enter second Number")
        self.Value2=int(input())

    def Addition(self):
        Ans=self.Value1+self.Value2
        return Ans
    
    def Substraction(self):
        Ans=self.Value1-self.Value2
        return Ans
    
    def Multiplication(self):
        Ans=self.Value1*self.Value2
        return Ans

    def Division(self):
        Ans=self.Value1/self.Value2
        return Ans
    


def main():
    obj1=Arthematic()

    obj1.Accept()

    Ret=obj1.Addition()
    print("Additon is:",Ret)

    Ret=obj1.Substraction()
    print("substration is:",Ret)

    Ret=obj1.Multiplication()
    print("Multiplication is:",Ret)

    Ret=obj1.Division()
    print("Division is:",Ret)
    


if __name__ == "__main__":
    main()
    

