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
def off():
    global start
    global flick
    shutdown()
    print('power turned off')
        # Writing to a file
    uptime = round((time.time()-start),2)
    with open('file.txt', 'a') as file:
        file.write((str(datetime.date)+str(datetime.time)+str(uptime)+'s'+'/n'))
        uptime = 0
        print(uptime)
    while not (sense() or flick):
        pass
    flick = False
    start = time.time()
def take(inp):
    global start, latest
    print('>>>',inp)
    if inp == 'on':
        flick = True
        noshutdown()
        flick = True
        start = time.time()
        latest= start
    elif inp =='off':
        off()
    elif inp=='peek':
        print(peek())
    elif inp=='power':
        power()
    elif inp=='upt':
        if peek():
            print('total uptime:',round(time.time()-start,2))
            print(round(MAXTIME-(time.time()-latest),2),'left')
        else:
            print(0)
    else:
        print('instruction not recognised')
def func():
    global latest

    if sense():
        print('sensing')
        latest= time.time()
       
        if not peek():
                noshutdown()
                print('power turned on')
    if time.time() - latest > MAXTIME:
        print('timeout')
        off()
        
        start = time.time()
    
def main_loop():
    while True:
        os.system('clear')
        current_date = datetime.now()
    
        day_of_week = current_date.strftime("%A")
        if day_of_week in weekdays:
            print(datetime.now().hour)
            while datetime.now().hour<6 or datetime.now().hour < 20:
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
        a = input()
        take(a)
        
thread = threading.Thread(target=main_loop,daemon=True)
thread.start()

inp()
main_loop()



