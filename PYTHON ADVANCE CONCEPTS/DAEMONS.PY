'''
A daemon thread is a thread which runs continuously in the background.
It provides support to non-daemon threads.

when any python program executed then default main thread start and all threads work under this main thread which is non deamon by default

When last non-daemon thread terminates, automatically all daemon threads
will be terminated. We are not required to terminate daemon thread explicitly.
'''

'''

CREATE DAEMON THREAD

setDaemon(True) Method or daemon = True Property is used to make a
thread a Daemon thread.


EXAMPLE --


'''

import threading


def fun1():
    print("hello")
    return

t1 = threading.Thread(target=fun1)
print(t1.daemon)
t1.daemon=True
print(t1.daemon)
# t1.setDaemon(True)
# t1.daemon = True


'''
setDaemon(True/False) - This method is used to set a thread as daemon thread.
You can set thread as daemon only before starting that thread which means active
thread/ status cann%t be changed as daemon.
If we pass True non-daemon thread will become daemon and if False daemon thread
will become non-daemon.



daemon Property - This property is used to check whether a thread is daemon or not. It
returns True if thread is daemon else False.
We can also use daemon property to set a thread as daemon thread or vice versa.


isDaemon() This method is used to check whether a thread is daemon or not. It returns
True if thread is daemon else False.
'''


from threading import current_thread,Thread

print(current_thread().name)


'''
Main Thread is always non-daemon thread.
Rest of the threads inheritsdaemon nature from their parents.
If parent thread is non daemorythen child thread will become non daemon thread.
If parent thread is daemon then child thread will also become a daemon thread.

'''

mt = current_thread()
print (mt.getName())
print('MT:',mt.isDaemon())
tl= Thread(target=fun1)
print('Tl Before: ',tl. isDaemon())
tl.setDaemon(True)
print('Tl After: ', tl.isDaemon())


'''
When last non-daemon thread terminates, automatically all daemon threads
will be terminated. We are not required to terminate daemon thread
explicitly.

'''


from multiprocessing import current_process,Process