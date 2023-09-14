import os
from sys import *

def CreateFile(FileName,Strx):
    if(os.path.exists(FileName)):
        fd=open(FileName,"r")
        text=fd.read()
        count=text.count(Strx)
        print("Frequency of word {} is {}".format(Strx,count))
      
        
    else:
        print(" File not exists")

def main():
    print("Wlcome to applications ;",argv[0])
    
    if(len(argv)!=3):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform  count freaquency of string into File")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide one number of argumnets as")
        print("First Argument as  FileName")
        print("Second Argument as String")
        exit()

    else:
        CreateFile(argv[1],argv[2])
    

    
if __name__ =="__main__":
    main()