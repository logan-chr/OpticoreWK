from testswitch import switch, noshutdown,shutdown,peek,power
from sensor import sense
import time
noshutdown()
MAXTIME = 10
timeout = MAXTIME
uptime = 0
while True:
    uptime += 1
    print(timeout)
    if timeout > 0:
        timeout -=1
    time.sleep(1)
    if sense():
        timeout = MAXTIME
        if not peek():
            noshutdown()
            print('power turned on')
    if timeout <= 0:
        shutdown()
        print('timeout, power turned off')
        # Writing to a file
        with open('file.txt', 'a') as file:
            file.write(str(str(uptime)+' '))
        uptime = 0
        while not sense():
            pass
        timeout = MAXTIME




