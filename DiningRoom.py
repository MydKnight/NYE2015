__author__ = 'madsens'

import Lights
import time
from subprocess import Popen, PIPE
import os
from DmxPy import DmxPy

# This code runs the Dining Room

dmx = DmxPy('/dev/ttyUSB0')
lastScan = 0
Lights.setup()

#Turn the reader back on.
os.system("/home/pi/Christmas-2015/Scripts/enableRFID.sh")

while True:    # Runs until break is encountered. We want to set it to break on a particular ID.
    n = raw_input("Scanned ID: ")
    currentScan = time.time()
    if n == "STOP":
        Lights.cleanup()
        break  # stops the loop
    else :
        #Turn off the reader until function finishes.
        os.system("/home/pi/Christmas-2015/Scripts/disableRFID.sh")

        Popen(['mpg321', '/home/pi/Christmas-2015/Assets/ChristmasOpener.mp3'], stdout=PIPE, close_fds=True)

        #Trigger GPIO Pins 33 to turn on project0r. Then wait 30 seconds for the audio to finish
        #Lights.off([37])
        #time.sleep(27)
        #Lights.on({37})

        #Do the DMX thing instead.
        dmx.setChannel(1, 255)
        dmx.setChannel(2, 255)
        dmx.setChannel(3, 255)
        dmx.setChannel(4, 255)
        dmx.render()

        time.sleep(27)
        dmx.setChannel(1, 0)
        dmx.setChannel(2, 0)
        dmx.setChannel(3, 0)
        dmx.setChannel(4, 0)
        dmx.render()

        #Turn the reader back on.
        os.system("/home/pi/Halloween2015/Scripts/enableRFID.sh")