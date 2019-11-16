from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
import time

button = Button(21, hold_time = 0.6)
end_time = 0
start_time = 0

def starttime():
    global start_time
    start_time = time.time()

def endtime():
    global end_time
    end_time = time.time()

def aorb():
    global button
    button.when_pressed = starttime
    button.when_released = endtime
    time_lapsed = end_time - start_time
    print(time_lapsed)

aorb()
pause()