__author__ = 'madsens'

import Logging
import os
import Movies

# This code runs the Dining Room
Logging.PowerLog()
print 'Starting'
Movies.StartLoop('/home/pi/NYE2015/Assets/DiningRoom')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    #Logging.HeartBeat()
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        Movies.StopLoop()
        print "Stopping."
        break  # stops the loop
    else :
        print "Playing."
        Logging.LogAccess(n)
        Movies.PlayMovie()