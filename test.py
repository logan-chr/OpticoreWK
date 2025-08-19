from testswitch import *
import threading
def inp():
    a = input()
    run(a)

while True:
    t1 = threading.Thread(target=inp)
    print('a')