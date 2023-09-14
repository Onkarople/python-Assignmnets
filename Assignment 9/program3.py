import os
from sys import *

def CreateFile(FileName):
    if(os.path.exists(FileName)):
        with open(FileName,"r") as FirstFile,open("Demo.txt","a") as SecondFile:
            for line in FirstFile:
                SecondFile.write(line)
    
        print("File copied Succesfully")
    else:
        print(" File Not Exixts")

def main():
    print("Wlcome to applications ;",argv[0])
    
    if(len(argv)!=2):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform  copy of one file to another")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide one number of argumnets as")
        print("First Argument as Application Name FileName")
        exit()

    else:
        CreateFile(argv[1])
    

        

   

if __name__ =="__main__":
    main()