import os
import psutil
from  sys import *
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



def ProcessDsiplay(log_dir="Marvellous"):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    separator="-" * 80
    log_path= os.path.join(log_dir,"MarvellousLog%s.log"%(time.strftime("%Y%m%d-%H%M%S")))
    f=open(log_path,'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystems Process Logger : "+time.ctime()+"\n")
    f.write(separator + "\n")


    for proc in psutil.process_iter():

       try:
      
         pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
         vms= proc.memory_full_info().vms/(1024*1024)
         pinfo['vms']=vms
         listprocess.append(pinfo)

       except(psutil. NoSuchProcess , psutil.AccessDenied, psutil.ZombieProcess):

         pass
    
    for element in listprocess:
        f.write("%s\n" % element)



def Sendmail(mailid):
    mail_content="hello Sir"
    
    sender_address = 'opleonkar@gmail.com'
    sender_pass = 'om77cool'
    receiver_address = mailid

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'

    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = 'MarvellousLog20221122-113315.log'
    attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload) #encode the attachment
    #add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')



def main():
    print("Marvellos infosystems ")

    print("Application name : "+argv[0])

    if(len(argv)!=3):
        print("Error:Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if(argv[1]=="-h") or (argv[1]=="-H"): 
        print("Help: This script is used to perform log record of running processes")
    
    elif(argv[1]=="-u") or (argv[1]=="-U"):
        print("Usage : ApplicationName AbsolutePath_Of_Directory")
        exit()
    
    try:
        ProcessDsiplay(argv[1])
        Sendmail(argv[2])
    except ValueError:
        print("Error:Inavalid Datatype of input")

    except Exception:
        print("Error:Invalid input")
    

if __name__=="__main__":
    main()


