from testswitch import switch
from sensor import sensor
import time
from datetime import datetime
import os
import threading
import csv
switch1 = switch()

MAXTIME = 60
timeout = MAXTIME
start = time.time()
latest = time.time()
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
flag = False
sensor1 = sensor()

def update_stats():
    global start
    if  switch1.peek():
        uptime = round((time.time()-start),2)
    else:
        uptime = 0
    total = uptime
    seconds_since_year_start = (datetime.now() - datetime(datetime.now().year, 1, 1)).total_seconds()


    with open('file.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            total += float(row[1])
    total = (total)
    saved = round(seconds_since_year_start-(total))

    add(str(str(round(0.394*(saved*15.4*2)/360,4))+'g'))
def add(array):
    
    if round(time.time())/3 == round(round(time.time())/3):
        with open('file.txt','w',newline='') as file:
            file.write(array)
def write(array):
    with open('file.csv','a',newline='') as file:
        writer  =csv.writer(file)
        writer.writerow((array))
def read():
    with open('file.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            
            print(row[0],': ',row[1])
def on():

    global start
    global latest
    global flag
    switch1.noshutdown()
    print('powering on')
    flag = True        

    start = time.time()

    latest= start
def off():
    update_stats()
    global length
    global start
    global flag
    w = float(switch1.power())
    switch1.shutdown()
    print('power turned off')
        # Writing to a file
    uptime = round((time.time()-start),2)
    print(round(w*uptime,2),' joules consumed')
    write([str(datetime.now())[:-7],uptime])
    
    uptime = 0
    start = time.time()
    
    print(uptime)
    print(flag)
    while (not(flag) and not(sensor.scan())):
        func()

        
    print('out')
    flag = False
    start = time.time()
def take(inp):
    global start, latest, flag
    os.system('clear')
    print('>>>'+inp)
    if inp == 'on':
        on()
    elif inp =='off':
        print('powering down...')
        off()
        start = time.time()
    elif inp=='peek':
        print(switch1.peek())
    elif inp=='power':
        print(switch1.power(),'W')
    elif inp=='upt':
        if switch1.peek():
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
        read()
    elif inp=='clear': 
        with open("file.csv", mode="w",newline='') as file:
            pass 

    elif inp=='total':
        total = 0
        with open('file.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                total += float(row[1])
        

                
        print('total uptime in history:',total)
        print('that\'s',round(total*15.4*2,4),'Joules')
        print('or',round((total*15.4*2)/360000,4),'Kilowatt Hours')
        print('or',round(0.394*(total*15.4*2)/360000,4),'Kg of Carbon Dioxide')
    elif inp=='saved':
        
        current_year_start = datetime(datetime.now().year, 1, 1)

        current_time = datetime.now()

        seconds_since_year_start = (current_time - current_year_start).total_seconds()
        total = 0
        with open('file.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                total += float(row[1])

        

        

    elif inp =='':
        print()
    elif inp=='reboot':
        switch1 = switch()
        flag = True
        off()
        on()
    else:
        update_stats()
        print(inp,'is not a known instruction')
def func():

    global start
    global latest
    global flag
    uptime = round((time.time()-start),2)
    if round(uptime/2,0) == uptime/2:


        update_stats()
    if sensor.scan():
        print('s')
        latest= time.time()
        flag = True
        if not switch1.peek():
            on()
    timedif = (time.time() - latest )
    if timedif > MAXTIME :
        flag = False
        if switch1.peek():

            print('timeout')
            off()

        start = time.time()    
def main_loop():
    while True:

        current_date = datetime.now()
        day_of_week = current_date.strftime("%A")
        if day_of_week in weekdays:
            
            while current_date.hour > 6 and current_date.hour < 20:
                func()
            while current_date.hour < 6 or current_date.hour > 20:
                if not switch1.peek():
                    print('port 3 and 5 has gone down, rebooting...')
                    switch1.noshutdown()
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



