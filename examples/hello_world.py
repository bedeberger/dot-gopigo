#!/usr/bin/env python

from time import sleep
from picamera import PiCamera
print "Hallo Kollegen"

camera = PiCamera()

camera.start_preview()
sleep (5)
camera.capture('/home/pi/Desktop/selfie.jpg')
camera.stop_preview()
