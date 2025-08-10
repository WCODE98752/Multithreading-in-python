import threading
import time


def fun1():
    time.sleep(5)
    print('Helle This is after 5s')
    
def fun2():
    time.sleep(6)
    print('This is after 6s')
    
    
    
a = threading.Thread(target=fun1)
b = threading.Thread(target=fun2)

a.start()
b.start()