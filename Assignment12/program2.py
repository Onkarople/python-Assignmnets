import psutil
from sys import *

def ProcessDisplay(PName):
   listprocess = []

   for proc in psutil.process_iter():

    try:
        if PName in proc.name():
            print(PName)
      

    except(psutil. NoSuchProcess , psutil.AccessDenied, psutil.ZombieProcess):

     pass

    

def main():
  print("Marvellous Infosystems : Python Automation & Machine Learning")

  print("Process Monitor")


  if(len(argv)!=2):
    print("Error:Insufficient arguments")
    print("Use -h for help and use -u for usage of the script")
    exit()

  if(argv[1]=="-h") or (argv[1]=="-H"): 
    print("Help: This script is used to perform Dsiplay process if its running ")
    
  elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : Provide one number of argumnets as")
        print("First Argument as name of process")
       
        exit()

  else:
    ProcessDisplay(argv[1])
       

if __name__ =="__main__":
    main()