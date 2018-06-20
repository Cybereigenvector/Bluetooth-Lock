##############################################################
# This program monitors for an authorized bluetooth device and#
# locks the screen of the notebook if the device is not       #
# present                                                     #
##############################################################
import bluetooth
import ctypes
import time
import sys

##############################################################
# The name of the authorized device is taken as an input in   #
# this block of code                                          #
##############################################################
Device_Name = raw_input("Enter the name of the authorized device that would be used with this Notebook \n")
print ("This device ", Device_Name, " has been sucessfully registered with the Notebook.\nPlease turn ON your mobile bluetooth")


##############################################################
# This function searches for the nearby bluetooth devices and #
# checks if the device being searched is in that list or not. #
# Hence it returns true or false accordinly                   #
##############################################################
def find_device(device):
    present = False
    try:
        nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)
        for addr, name in nearby_devices:
            if name == Device_Name and bluetooth.find_service(address=addr) != []:
                present = True
                return present
        return present
    except IOError:
        print ("No device found!!\nMake your bluetooth discoverable\n")
        time.sleep(3)
        return False


##############################################################
# This function starts the monitoring process once the        #
# required device is detected. If the device gets disconnected#
# then this function locks the screen of the computer         #
##############################################################
def monitor_registered_device(search):
    print ("Device ", Device_Name, "Connected!! \nMonitoring...... \n")
    while (1):
        track = find_device(search)
        print (Device_Name, "is still connected to this notebook")
        if track == False:
            print ("No registered device found!!\nLocking computer in 5 seconds")
            time.sleep(5)
            ctypes.windll.user32.LockWorkStation()
            break


###############################################################
# The main body of the program.This function calls other       #
# necessary functions to make the program work.	              #
###############################################################
while (1):
    if (find_device(Device_Name)):
        monitor_registered_device(Device_Name)
    print ("\nSearching...")
