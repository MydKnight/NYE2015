__author__ = 'madsens'

import Logging
import os
import Movies
import time
import Lights

# This code runs the Furnace
Lights.setup2()

Logging.PowerLog()
print 'Starting'
Movies.StartLoop('/home/pi/NYE2015/Assets/Furnace')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    #Logging.HeartBeat()
    n = raw_input("Scanned ID: ")
    Lights.showColor("gold")
    if n == "STOP":
        Movies.StopLoop()
        Lights.cleanup()
        print "Stopping."
        break  # stops the loop
    else :
        # On Input, Disable Reader
        os.system("/home/pi/NYE2015/Scripts/disableRFID.sh")
        Lights.showColor("red")
        time.sleep(2)
        Lights.showColor("none")
        print "Playing."
        Logging.LogAccess(n)
        Movies.PlayMovie()

        time.sleep(60)

        # Reenable reader.
        os.system("/home/pi/NYE2015/Scripts/enableRFID.sh")