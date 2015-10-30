#  _____   __     __  ___     _____   __  __    _____ 
# |  __ \  \ \   / / |__ \   / ____| |  \/  |  / ____|
# | |__) |  \ \_/ /     ) | | (___   | \  / | | (___  
# |  ___/    \   /     / /   \___ \  | |\/| |  \___ \ 
# | |         | |     / /_   ____) | | |  | |  ____) |
# |_|         |_|    |____| |_____/  |_|  |_| |_____/ 
#                                                     
                                                   

import os

def sms(pnumber,msg):
    sysmsg = 'curl http://textbelt.com/text -d number=' + str(pnumber) + ' -d ' + '\"message=' + str(msg) + '\"'
    os.system(sysmsg)
    print("Message: " + msg + " sent to phone number: " + str(pnumber))

# To send a text message call the function with
# sms(phonenumber,'sending this text message')
# sms(5551235555,'Hello World!')
