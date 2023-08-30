
# use SMTP
import smtplib
temp=0
def spoof_mail(fake_name,to_email,subject,content):
    
    # set username and password for the email server to connect and send mails 
    
    username = ('')
    password = ('')

    # set fake email sender adress and name 
    fake_from = "xyz@gmail.com"
    # fake_name = "Donald Trump"



    # # set email receiver email adress & name
    
    # to_email = "ufree018@gmail.com"



    # set subject
    # subject = "Spoofing Test "
    # content = "This is not from Fake Name. It is demo how to fake a sender email adress"

    # build the complete email message from all variables
    message = f"From: {fake_name} <{fake_from}>\nTo: {to_email}\nSubject: {subject}\n\n{content}"

    # show the email message for debuging
    print(message)

    # set the email Server and Network Port here it is gmail 
    server = smtplib.SMTP("smtp.gmail.com", 587)

    # set secure sending 
    server.starttls()

    # login into the email server
    server.login(username, password)

    # send the message
    server.sendmail(fake_name, to_email, message )

    # close mail server connection 
    server.close()

    

    print('sent')
temp=1
    
