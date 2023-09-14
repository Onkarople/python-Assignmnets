#object oriented concepts

class Demo:
    Value=0
    def __init__(self,A,B):
        self.No1=A
        self.No2=B

    def Fun(self):
        print("Instance variable of Fun method",self.No1)
        print("Instace variable of Fun method",self.No2)
    
    def Gun(self):
        print("Instance variable of Gun method",self.No1)
        print("Instace variable of Gun method",self.No2)
        


def main():
    obj1=Demo(11,21)
    obj2=Demo(51,101)

    print("Fun method by using both objects ")

    obj1.Fun()
    obj2.Fun()

    print("_____________________________________")

    print("Gun method by using both objects")
    

    obj1.Gun()
    obj2.Gun()


if __name__ == "__main__":
    main()