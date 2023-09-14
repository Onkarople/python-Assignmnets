import os

def CreateFile(FileName):
    if(os.path.exists(FileName)):
        fd=open(FileName,"r")

        print("Contents of file is:")
        print(fd.read())
       
    else:
        print("Not Exixts")

def main():
    print("Enter the file name")
    Name = input()

    CreateFile(Name)

if __name__ =="__main__":
    main()