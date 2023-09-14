#Display pattern


def Display(No):
    for i in range(0,No):
        for j in range(0,No):
            print("*",end=" ")
        
        print()
    
def main():
    print("Enter number")
    No=int(input())
    Display(No)

if __name__ =="__main__":
    main()