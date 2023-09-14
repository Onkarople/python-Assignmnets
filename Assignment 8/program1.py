
def Dsiplay(No):
    if(No!=0):
        print(" * ",end=" ")
        No=No-1
        Dsiplay(No)

def main():
    print("Enter Number")
    No=int(input())
    Dsiplay(No)
    


if __name__ == "__main__":
    main()