import os
import time

tv_off = True

def turn_on_tv():
    os.system('echo "on 0" | cec-client -s -d 1')
    tv_off = False

def turn_off_tv():
    os.system('echo "standby 0" | cec-client -s -d 1')


while True:
    current_time = time.localtime()

    # Check if it's 8 AM
    if current_time.tm_hour >= 8 and current_time.tm_hour <= 17 :
        if(tv_off):
            turn_on_tv()     
    # Check if it's 5 PM
    else:
        if(not tv_off):
                turn_off_tv()

    # Sleep for an hours avoid excessive CPU usage
    time.sleep(15*60)