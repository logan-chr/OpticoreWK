from testswitch import switch, noshutdown,shutdown,peek,power,run
from sensor import sense
import time
from datetime import datetime
import keyboard
import os
import threading


noshutdown()
MAXTIME = 30
timeout = MAXTIME
start = time.time()
latest = time.time()
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
flick = False

def on():
    global start
    global latest
    global flick
    noshutdown()
    print('powering on')
    flick = True        

    start = time.time()

    latest= start
def off():
    global start
    global flick
    w = float(power())
    shutdown()
    print('power turned off')
        # Writing to a file
    uptime = round((time.time()-start),2)
    print(round(w*uptime,2),' joules consumed')
    file = open('file.txt', 'a')
    file.write((str(datetime.now())[:-7]+' UPT:'+str(uptime)+'s'+'\n'))
    uptime = 0
    print(uptime)
   
    while not (sense() or flick):

        inp()
     
    
    flick = False
    start = time.time()
def take(inp):
    global start, latest, flick
    os.system('clear')
    print('>>>'+inp)
    if inp == 'on':
        on()
    elif inp =='off':
        print('powering down...')
        off()
        start = time.time()
    elif inp=='peek':
        print(peek())
    elif inp=='power':
        print(power(),'W')
    elif inp=='upt':
        if peek():
            print('total uptime:',round(time.time()-start,2))
            print(round(MAXTIME-(time.time()-latest),2),'left')
        else:
            print(0)
    elif inp=='help':
        print()
        print('instructions:')
        print()
        print('on\noff\npeek\npower\nupt (uptime)\nhistory\nclear')
    elif inp=='history':
        with open('file.txt', 'r') as file:
            content = file.read()
            print(content)
    elif inp=='clear':
        with open("file.txt", "w") as file:
            pass 
    elif inp=='total':
        total = 0
        f = open('file.txt','r')
        lines = f.readlines()
        for i in range(len(lines)):
            total += (float((lines[i].replace('s','')[24:]).replace("\n", "")))
        print('total uptime in history:',total)
        print('that\'s',total*15.4,'W')
    else:
        print('instruction not recognised')
def func():
   
    global latest

    if sense():
        
        latest= time.time()
   
        if not peek():
            on()
    timedif = (time.time() - latest )
    if timedif > MAXTIME:
        print('timeout')
        off()

        start = time.time()    
def main_loop():
    while True:

        current_date = datetime.now()
        day_of_week = current_date.strftime("%A")
        if day_of_week in weekdays:
            
            while datetime.now().hour>6 and datetime.now().hour < 20:
                func()
            while datetime.now().hour<6 or datetime.now().hour > 20:
                if not peek():
                    print('port fa/03 has gone down, rebooting...')
                    noshutdown()
                print('work hours')
        else:
            print('func')
            func()
def inp():
    while True:
        print('>>>',end='')
        a = input()
        take(a)

os.system('clear')
thread = threading.Thread(target=main_loop,daemon=True)

thread.start()

inp()
main_loop()



