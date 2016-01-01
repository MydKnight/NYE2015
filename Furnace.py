__author__ = 'madsens'

import Logging
import os
import Movies
import time

# This code runs the Dining Room
Logging.PowerLog()
print 'Starting'
Movies.StartLoop('/home/pi/NYE2015/Assets/Furnace')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    #Logging.HeartBeat()
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        Movies.StopLoop()
        print "Stopping."
        break  # stops the loop
    else :
        # On Input, Disable Reader
        os.system("/home/pi/NYE2015/Scripts/disableRFID.sh")
        print "Playing."
        Logging.LogAccess(n)
        Movies.PlayMovie()

        time.sleep(60)

        # On Input, Disable Reader
        os.system("/home/pi/NYE2015/Scripts/enableRFID.sh")