from gpiozero import Button
from subprocess import check_call
from signal import pause
import os
import time
import _thread as thr

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
}

current_letter = ""
current_word = []
tick = 0
button = Button(21) # The button
cool_lock = thr.allocate_lock()


def decodeAlexandre(message):
    for i in message:
        if i in list(MORSE_CODE_DICT.values()):
            for K in MORSE_CODE_DICT:
                if MORSE_CODE_DICT[K] == i:
                    print(K, end = "")
    print('')

def ditordot():
    global current_letter
    global tick
    global cool_lock
    global current_word
    with cool_lock:
        if tick>= 7:
            tick = 0
            print("  ", end = "")
            current_word.append(current_letter)
            print(current_word)
            decodeAlexandre(current_word)
            current_word = []
        if tick >= 3 and tick <= 7:
            tick = 0
            print(" ", end = "")
            current_word.append(current_letter)
            current_letter = ""
    ditlength = 0.15#if the button press is less than this length, it will be a dit, else a dot
    badlength = 0.009
    global button
    presslength = 0
    while button.is_pressed:
        presslength = button.pressed_time
    if presslength < badlength:
        pass
    elif presslength < ditlength:
        print(".", end = "")
        current_letter += "."
    else:
        print("-", end = "")
        current_letter += "-"
    with cool_lock:
        tick = 0

button.when_pressed = ditordot


def threadfunction():
    global tick
    print("HERE")
    while True:
        time.sleep(0.15)
        with cool_lock:
            tick += 1
            
            
thr.start_new_thread(threadfunction, ()) 
