import os

def CreateFile(FileName):
    if(os.path.exists(FileName)):
        print("File is already exsiting")
        return
    else:
        print("Not Exixts")

def main():
    print("Enter the file name")
    Name = input()

    CreateFile(Name)

if __name__ =="__main__":
    main()