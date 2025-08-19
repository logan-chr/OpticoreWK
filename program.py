from testswitch import switch, noshutdown,shutdown,peek,power
from sensor import sense
import time
noshutdown()
timeout = 30
while True:
    print(timeout)
    if timeout > 0:
        timeout -=1
    time.sleep(1)
    if sense():
        timeout = 30
        if not peek():
            noshutdown()
            print('power turned on')
    if timeout <= 0:
        shutdown()
        print('timeout, power turned off')
        while not sense():
            pass



