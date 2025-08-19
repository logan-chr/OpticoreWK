from testswitch import switch, noshutdown,shutdown,peek,power,run
from sensor import sense
import time
from datetime import datetime
import keyboard
import os
import threading
import pandas as pd
import csv

noshutdown()
MAXTIME = 30
timeout = MAXTIME
start = time.time()
latest = time.time()
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
flick = False


with open('file.csv', 'r') as file:
    reader = csv.reader(file)
    length = sum(1 for row in reader) - 1
    
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
    global length
    global start
    global flick
    w = float(power())
    shutdown()
    print('power turned off')
        # Writing to a file
    uptime = round((time.time()-start),2)
    print(round(w*uptime,2),' joules consumed')
    with open('file.csv', mode='a',newline='',encoding='utf-8') as file:
        writer  =csv.writer(file)
        writer.writerow(pd.DataFrame({'date':str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')),'uptime':(uptime)},index=[length]))
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
        print('on\noff\npeek\npower\nupt (uptime)\nhistory\nclear\ntotal')
    elif inp=='history':
        with open('file.csv', mode='r',newline='') as file:
            print('h')
            if os.path.getsize('file.csv') > 0:
                content = pd.read_csv('file.csv',encoding='utf-8')

                print(content)
            else:
                print()
    elif inp=='clear': 
        with open("file.csv", mode="w",newline='') as file:
            pass 
    elif inp=='total':
        total = 0
        with open('file.csv', mode='r',newline='') as file:
            print('h')
            if os.path.getsize('file.csv') > 0:
                content = pd.read_csv('file.csv',encoding='utf-8')

                
            total += (float((lines[i].replace('s','')[24:]).replace("\n", "")))
        print('total uptime in history:',total)
        print('that\'s',round(total*15.4,4),'W')
    elif inp =='':
        print()
    else:
        print(inp,'is not a known instruction')
def func():
   
    global latest

    if sense():
        print('s')
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



