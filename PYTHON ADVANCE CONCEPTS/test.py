
from threading import Thread
def display():
    for i in range(5):
        print("hello world!")

t1 = Thread(target=display)
t2 = Thread(target=display)
t1.start()
t2.start()