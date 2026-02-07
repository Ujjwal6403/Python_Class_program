#==================================================
# Program : Simple Gmail Mail Sender
# Author : Ujjwal narkhede 
# Purpose : Send mail using Python SMTP
#==================================================

import smtplib
from email.message import EmailMessage

#--------------------------------------------------
#Function :        Marvellous_send_mail
#Description :     Send email using Gmail SMTP Server
#--------------------------------------------------

def Marvellous_send_mail(sender,app_password,receiver,subject,body):
   #Step 1: create Email object 
   msg = EmailMessage()
   
   #Step 2: Set mail Headers
   msg["From"] = sender
   msg["To"] = receiver
   msg["Subject"] = subject
   
   #Step 3: Add mail body
   msg.set_content(body)
   
   
   #Step 4 : Create SMTP SSL Connection manually
   smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
   
   #Step 5: Login usign Gmail+App Password
   smtp.login(sender,app_password)
   
   #step 6 : Send the email
   smtp.send_message(msg)
   
   #Step 7 : Close connection manually
   smtp.quit()
   
   #------------------------------------------------
   # Function :     main
   # Description :   Driver Code
   #------------------------------------------------
   
def main():
#Always use separate temporary/testing account
   sender_mail = "ujwal443103@gmail.com"
      
# App Password generated from Google Account
   app_passowrd = "jmwh jjya qrei zwzr"
   
# Your second email for testing 
   receiver_email = "marvellousinfosystem@gmail.com"
   
   
   Subject = "Test mail from python Script"
   
   body = """Jay Ganesh...this is a test email sent using Marvellous python
   Regards,
   marvellous infosystems
   """
   Marvellous_send_mail(sender_mail,app_passowrd,receiver_email,Subject,body)
   
   print("Marvellous mail sent successfully")

#----------------------------------------------------
# Program Entry point
#---------------------------------------------------
if __name__ == "__main__":
   main()