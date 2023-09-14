
class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    
    def Accept(self):
        print("Enter Radius of Circle")
        self.Radius=int(input())

    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius
    
    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius
    

    def Display(self):
        print("Radius of circle is",self.Radius)
        print("Area of circle is",self.Area)
        print("Circumference of circle is ",self.Circumference)


def main():
    obj1=Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    


if __name__ == "__main__":
    main()
