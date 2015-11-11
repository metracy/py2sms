'''
88888888ba              ad888888b,  ad88888ba  88b           d88  ad88888ba   
88      "8b            d8"     "88 d8"     "8b 888b         d888 d8"     "8b  
88      ,8P                    a8P Y8,         88`8b       d8'88 Y8,          
88aaaaaa8P' 8b       d8     ,d8P"  `Y8aaaaa,   88 `8b     d8' 88 `Y8aaaaa,    
88""""""'   `8b     d8'   a8P"       `"""""8b, 88  `8b   d8'  88   `"""""8b,  
88           `8b   d8'  a8P'               `8b 88   `8b d8'   88         `8b  
88            `8b,d8'  d8"         Y8a     a8P 88    `888'    88 Y8a     a8P  
88              Y88'   88888888888  "Y88888P"  88     `8'     88  "Y88888P"   
                d8'                                                           
               d8'    
'''                                                   

import subprocess as sp
#YOU WILL NEED TO CHANGE THE BELOW TO YOUR KEY AND YOUR SECRET AFTER YOU REGISTER WITH SINCH.
#REGISTER for free at https://www.sinch.com/products/sms-api/ <----------- pretty easy

key = '549e8c36-0ff9-49dd-87e8-02cbac532c3a' #your key here
secret = 'EEHQnEBLtUGwzJdf+OWA1w==' #your secret here

sysmsg = ['curl','--user','key:secret','--data','msg','-H','\'Content-Type: application/json\'','phoneurl']
sysmsg[2] = '\"application\\%s:%s\"' % (key, secret)

#PUT the country code in front of phone number, I've only tested this with 1 for America. Because we #1 it works.
def sms(pnumber,msg):
    sysmsg[4] = '\'{\"message\":\"%s\"}\'' % (str(msg))
    sysmsg[7] = 'https://messagingapi.sinch.com/v1/sms/%s' % (str(pnumber))
    fsysmsg = " ".join(sysmsg)
    mstatus = sp.check_output(fsysmsg, shell = True)
    if mstatus[:12] == '{"messageId"':
        print(mstatus[1:22].upper() + "   MSG: %s.   SENTTO: %s" % (msg, str(pnumber)))
    else:
        print('Error Received: ' + mstatus)

# To send a text message call the function with
# sms(phonenumber,'sending this text message')
# sms(15551235555,'Hello World!')
