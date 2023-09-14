
def Dsiplay(No):
    if(No!=0):
        No=No-1
        Dsiplay(No)
        print(No,end=" ")
        

def main():
    print("Enter Number")
    No=int(input())
    Dsiplay(No)
    


if __name__ == "__main__":
    main()