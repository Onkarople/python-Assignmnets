#Display pattern


def Display(No):
    x=No
    for i in range(0,No):
        for j in range(0,x):
            print("*",end=" ")
        
        x=x-1
        
        print()
    
def main():
    print("Enter number")
    No=int(input())
    Display(No)

if __name__ =="__main__":
    main()