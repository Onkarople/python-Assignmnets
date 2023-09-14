import os
from sys import *
import filecmp

def CreateFile(FileName1,FileName2):
    result=False
    if(os.path.exists(FileName1)):
        if(os.path.exists(FileName2)):
          result=filecmp.cmp(FileName1,FileName2,shallow=False)

        if(result==0):
            print("Succesfully")
        else:
            print("Failure")
   
    else:
        print(" File not exists")

def main():
    print("Wlcome to applications ;",argv[0])
    
    if(len(argv)!=3):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform  comaprision of one file to another")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide one number of argumnets as")
        print("First Argument as Application Name FileName")
        exit()

    else:
        CreateFile(argv[1],argv[2])
    

        

   

if __name__ =="__main__":
    main()