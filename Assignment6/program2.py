

class BankAccount:
    ROI=10.5

    def __init__(self):
        self.Name=""
        self.Amount=0
    
    def Accept(self):
        print("Enter the Name")
        self.Name=input()

        print("Enter Amount")
        self.Amount=int(input())

    def Display(self):
        print("Name is:",self.Name)
        print("Amount is:",self.Amount)
    
    def Deposit(self,value):
        self.Amount=self.Amount+value
    
    def withdraw(self,value):
        self.Amount=self.Amount-value
    
    def CalculateIntresr(self,time):
        Interst=(self.Amount*BankAccount.ROI*time)
        return Interst/100


def main():
    obj1=BankAccount()
    obj1.Accept()

    obj1.Display()

    obj1.Deposit(1000)

    print("Amount after deposit is:",obj1.Amount)

    obj1.withdraw(200)

    print("Amount after withdraw : ",obj1.Amount)

    Ret=obj1.CalculateIntresr(2)

    print("Intersrt is :",Ret)


if __name__ == "__main__":
    main()