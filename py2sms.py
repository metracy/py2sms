'''
d8888b. db    db .d888b. .d8888. .88b  d88. .d8888. 
88  `8D `8b  d8' VP  `8D 88'  YP 88'YbdP`88 88'  YP 
88oodD'  `8bd8'     odD' `8bo.   88  88  88 `8bo.   
88~~~      88     .88'     `Y8b. 88  88  88   `Y8b. 
88         88    j88.    db   8D 88  88  88 db   8D 
88         YP    888888D `8888Y' YP  YP  YP `8888Y'  
'''                                                   

import subprocess as sp
#YOU WILL NEED TO CHANGE THE BELOW TO YOUR KEY AND YOUR SECRET AFTER YOU REGISTER WITH SINCH.COM
key = '549e8c36-0ff9-49dd-87e8-02cbac532c3a' #your key here
secret = 'EEHQnEBLtUGwzJdf+OWA1w==' #your secret here

sysmsg = ['curl','--user','key:secret','--data','msg','-H','\'Content-Type: application/json\'','phoneurl']
sysmsg[2] = '\"application\\%s:%s\"' % (key, secret)

def sms(pnumber,msg):
    sysmsg[4] = '\'{\"message\":\"%s\"}\'' % (str(msg))
    sysmsg[7] = 'https://messagingapi.sinch.com/v1/sms/%s' % (str(pnumber))
    sp.call(" ".join(sysmsg), shell = True)
    ##subprocess.check_output returns a string of output of the command too
    ##useful if you want to check the value returned to verify if the message sent
    #output = subprocess.check_output(sysmsg.split(' '))
    #if 'error' in output.lower():
    #    print("Message: " + message + " failed to send to " + str(pnumber))
    #elif 'false' in output.lower():
    #    print("Message: " + message + " failed to send to " + str(pnumber))
    print("Message: " + msg + " sent to phone number: " + str(pnumber))

# To send a text message call the function with
# sms(phonenumber,'sending this text message')
# sms(5551235555,'Hello World!')
