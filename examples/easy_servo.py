#!/usr/bin/env python

import easygopigo3 as easy
import time

gpg = easy.EasyGoPiGo3()
servo = gpg.init_servo("SERVO1")

servo.rotate_servo(90)
