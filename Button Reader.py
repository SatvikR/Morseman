from gpiozero import Button
import time
import _thread as thr
import turtle

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
   '(':'-.--.', ')':'-.--.-', " ":" "
}
T = turtle.Turtle()
turtle.setup(960, 1080)
turtle.hideturtle()
turtle.write("Start Tapping! Click When Ready!", font=("Arial", 30), align="center")
T.hideturtle()

current_letter = ""
current_word = []
tick = 0
button = Button(21) # The button
cool_lock = thr.allocate_lock()
total_message = ""
currentsentence = ""
current_buffer = []

def decode(message):
    global currentsentence
    for i in message:
        if i in list(MORSE_CODE_DICT.values()):
            for K in MORSE_CODE_DICT:
                if MORSE_CODE_DICT[K] == i:
                    currentsentence = currentsentence + K
def dump(x, y): #DUMPS MESSAGE
    global tick
    global current_buffer
    global current_word
    global current_letter
    global currentsentence
    global cool_lock
    global T
    
    #print("I HAPPENED")
    print(current_buffer)
    with cool_lock:
        current_word.append(current_letter)
        current_buffer.append(current_word)
        tick = 0 
        for word in current_buffer:
            decode(word)
        T.clear()
        turtle.clear()
        T.write(currentsentence, font=("Arial", 60), align="center")
        currentsentence = ""
        current_buffer = []
        current_word = []
        current_letter = ""
        

def ditordot():
    global current_letter
    global tick
    global cool_lock
    global current_word
    global currentsentence
    global current_buffer
    with cool_lock:
        if tick > 7:
            tick = 0
            print(" ", end = "")
            current_word.append(current_letter)
            current_buffer.append(current_word)
            #print("WORD", current_word)
            #print("BUFFER", current_buffer)
            current_letter = ""
            current_word = []
            
        if tick >= 3 and tick <= 7:
            tick = 0
            #print(current_word)
            #print(current_letter)
            current_word.append(current_letter)
            current_letter = ""
            print(" ", end = "")
            
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
#you cannot hear the bass in metal

def threadfunction():
    global tick
    print("START TAPPING!!")
    while True:
        time.sleep(0.15)
        with cool_lock:
            tick += 1
            

                
thr.start_new_thread(threadfunction, ())
#thr.start_new_thread(readerboard, ())
turtle.onscreenclick(dump)
turtle.mainloop()
while True:
    pass

