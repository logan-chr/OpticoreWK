from testswitch import switch, noshutdown,shutdown,peek,power,run
from sensor import sense
import time
from datetime import datetime
import keyboard
noshutdown()
MAXTIME = 10
timeout = MAXTIME
start = time.time()
latest = time.time()
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday']
def off():
    shutdown()
    print('timeout, power turned off')
        # Writing to a file
    uptime = round((time.time()-start),2)
    print(uptime)
    with open('file.txt', 'a') as file:
        file.write(str(str(uptime)+'s'))
    while not sense():
        pass
def take(inp):
    print('>>>',inp)
    if inp == 'on':
        noshutdown()
    elif inp =='off':
        shutdown()
    elif inp=='peek':
        peek()
    elif inp=='power':
        power()
    elif inp=='upt':
        print('total uptime:',round(time.time()-start,2))
        print(round(MAXTIME-(time.time()-latest),2),'left')
    else:
        print('instruction not recognised')
def func():
    if sense():
        print('sensing')
        latest= time.time()
       
        if not peek():
                noshutdown()
                print('power turned on')
    if time.time() - latest > MAXTIME:
        off()
        
        start = time.time()
while True:
    current_date = datetime.now()
    
    day_of_week = current_date.strftime("%A")
    if day_of_week in weekdays:
        
        while datetime.now().hour<6 or datetime.now().hour > 20:
            func()
    else:
        print('work hours')
        
    




