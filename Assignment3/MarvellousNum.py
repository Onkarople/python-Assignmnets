def ChkPrime(No):
    i=0
    for i in range(2,int(No/2)+1,1):
        if(No%i==0):
            break


    if i == int(No/2):
        return No
   