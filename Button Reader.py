from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
import time
import time

tick = 0
button = Button(21) # The button

def ditordot():
    global tick
    tick = 0
    ditlength = 0.15#if the button press is less than this length, it will be a dit, else a dot
    badlength = 0.009
    global button
    presslength = 0
    while button.is_pressed:
        presslength = button.pressed_time
    if presslength < badlength:
        pass
    elif presslength < ditlength:
        print(".", end = " ")
    else:
        print("_", end = " ")

button.when_pressed = ditordot

while True:
    time.sleep(0.15)
    tick += 1
    if tick >= 3 and tick <= 7:
        print(" ", end = "")
        tick = 0
    
