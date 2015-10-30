#  _____   __     __  ___     _____   __  __    _____ 
# |  __ \  \ \   / / |__ \   / ____| |  \/  |  / ____|
# | |__) |  \ \_/ /     ) | | (___   | \  / | | (___  
# |  ___/    \   /     / /   \___ \  | |\/| |  \___ \ 
# | |         | |     / /_   ____) | | |  | |  ____) |
# |_|         |_|    |____| |_____/  |_|  |_| |_____/ 
#                                                     
                                                   

import subprocess

def sms(pnumber,msg):
    sysmsg = 'curl http://textbelt.com/text -d number=' + str(pnumber) + ' -d ' + '\"message=' + str(msg) + '\"'
    subprocess.call(sysmsg.split(' '))
    ##subprocess.check_output returns a string of output of the command too
    ##useful if you want to check the value returned to verify if the message sent
    #output = subprocess.check_output(sysmsg.split(' '))
    #if 'error' in output.lower():
    #    print("Message: " + message + " failed to send to " + str(pnumber))
    #else:
    print("Message: " + msg + " sent to phone number: " + str(pnumber))

# To send a text message call the function with
# sms(phonenumber,'sending this text message')
# sms(5551235555,'Hello World!')
