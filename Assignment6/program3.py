
class Numbers:
    def __init__(self,value):
        self.Value=value

    
    def Factors(self):

        for i in range(1,(self.Value//2)+1):
            if(self.Value%i==0):
                print("Factor is:",i)
    

    def SumFactors(self):
        sum=0
        for i in range(1,(self.Value//2)+1):
            if(self.Value%i==0):
                sum=sum+i
        
        
        return sum


    def ChkPerfect(self):
        No=self.SumFactors()
        if self.Value==No:
            return True

        else:
            return False    


    
    def Chkprime(self):
        bFlag=True

        for i in range(2,(self.Value//2)+1):
            if (self.Value % i==0):
                bFlag=False
                break
        
        return bFlag



def main():

    obj1=Numbers(7)
    bRet=obj1.Chkprime()
    if(bRet==True):
        print("Is prime")
    else:
        print("Is Not Prime")
    
    bRet=obj1.ChkPerfect()
    if(bRet==True):
        print("Is perfect")
    else:
        print("Is Not Perfect")
    
    obj1.Factors()

    Ans=obj1.SumFactors()

    print("Sum is:",Ans)
    


if __name__ == "__main__":
    main()
