__author__ = 'madsens'
import Movies
import Logging

Logging.PowerLog()
print 'Starting'
Movies.StartLoop('/home/pi/Christmas-2015/Assets/Fireplace')

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    Logging.HeartBeat()
    n = raw_input("Scanned ID: ")
    if n == "STOP":
        Movies.StopLoop()
        print "Stopping."
        break  # stops the loop
    else :
        print "Playing."
        Movies.PlayMovie()