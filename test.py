from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
import time
import pygame

pygame.mixer.init()
button = Button(21)
end_time = 0
start_time = 0
did_time_end = False
no = 0.0001 #less than = error
dit = 0.3 #less than

def starttime():
    global start_time
    start_time = time.time()

def endtime():
    global end_time
    end_time = time.time()

def aorb():
    global button
    button.wait_for_press()
    button.wait_for_release()
    time_lapsed = end_time - start_time
    if time_lapsed < no:
        print("ERROR")
    elif time_lapsed > dit:
        print("_", end = "")
        pygame.mixer.music.load("Long.wav")
        pygame.mixer.music.play()
    else:
        print(".", end = "")
        pygame.mixer.music.load("Short.wav")
        pygame.mixer.music.play()

button.when_pressed = starttime
button.when_released = endtime
while True:
    aorb()
pause()