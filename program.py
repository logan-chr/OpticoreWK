from testswitch import switch, noshutdown,shutdown,peek,power
from sensor import sense
import time
from datetime import datetime
noshutdown()
MAXTIME = 10
timeout = MAXTIME
start = time.time()
print(start)
latest = time.time()
while True:
    if sense():
        latest= time.time()
       
        if not peek():
            noshutdown()
            print('power turned on')
    if time.time() - latest > MAXTIME:
        shutdown()
        print('timeout, power turned off')
        # Writing to a file
        uptime = round((time.time()-start),2)
        print(uptime)
        with open('file.txt', 'a') as file:
            file.write(str(str(uptime)+'s'))
        while not sense():
            pass
        
        start = time.time()
    




