from sys import *
import os
import fnmatch
from glob import glob
from pathlib import Path

def DirectoryRename(Directoryname,Ext1,Ext2):
    for foldername,subfolder,Filenames in os.walk(Directoryname):
      
        for fnames in Filenames:
            s=fnames.split('.')

            filepath = foldername
                
            if s[1]==Ext1[1:]:
                base = os.path.splitext(fnames)[0]
                file_path = os.path.join(filepath, fnames)
                new_name = os.path.join(filepath, base + Ext2)
                os.rename(file_path, new_name)

            

        
        print(" ")

       
        


def main():
    print("----------------Marvellous Infosystems Automations------------")

    print("Automation script started with name :",argv[0])

    if(len(argv)!=4):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform convert one  extensions to other")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide 2 number of argumnets as")
        print("First Argument as Directory name")
        print("Second Argument as : Extension")
        print("Third Argument as : Extension")

        exit()

    else:
        DirectoryRename(argv[1],argv[2],argv[3])

   
if __name__=="__main__":
    main()