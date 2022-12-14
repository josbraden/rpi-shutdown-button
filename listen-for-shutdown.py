#!/usr/bin/env python
# Using GPIO 18 for my project
# Place file under /usr/local/bin/ and mark executable

import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(18, GPIO.FALLING)
subprocess.call(['shutdown', '-h', 'now'], shell=False)
