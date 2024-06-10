''' __ QUEUE __ 

* Linear Data Structure
* Follows FIFO : First In First Out
* Insertion can take place from the rear end.
* Deletion can take place from the front end.
* Eg: queue at ticket counters, bus station


Funtions -- 4 major operations:

o enqueue(element) - used to insert element at top
o dequeue() - removes the top element from queue
o peekfirst() - to get the first element of queue
o peeklast() - to get the last element of queue

All operation works in constant time i.e, 0(1)

'''




# class Queue:
#   def __init__(self):
#     self.queue = []
#   def enqueue(self,item):
#     self.queue.append(item)
#   def dequeue(self):
#     if len(self.queue) < 1:
#       return None
#     return self.queue.pop(0)
#   def display(self):
#     print(self.queue)
#   def size(self):
#     return len(self.queue)
  

# q=Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.display()
# q.dequeue()
# q.enqueue(5)
# q.display()
# print(type(q))










# circular queue


# q=[]
# q.append(1)
# q.append(2)
# q.append(3)
# q.pop(0)
# q.append(4)
# print(q)



















# implementing / creating Queue class using deque class and its functions
'''
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()  # creating instance of class
    
    def enqueue(self,val):   # creating queue 1st function which will insert element 
        self.buffer.appendleft(val)  # using appendleft from deque

    def dequeue(self):       # creating dequeue function which will remove element from queue
        return self.buffer.pop()  # using pop from deque
    
    def is_empty(self):        # creating is_empty function which will return if queue is empty
        return len(self.buffer) == 0  # return true if queue is empty else false
    
    def size(self):            # creting size function which will return size of the queue
        return len(self.buffer)  # return size



a=Queue()

a.enqueue({
    'Name':'Paras Dattera',
    'Age':'22',
    'Roll no':2319020
})

a.enqueue({
    'Name':'Ripu',
    'Age':'22',
    'Roll no':2319007
})

a.enqueue({
    'Name':'Vivek',
    'Age':'21',
    'Roll no':2319025
})


'''




















# queue can be implemented using list as well just use 0 and insert function it will work like fifo and queue


# queue = []
# queue.insert(0,1)
# queue.insert(0,2)
# queue.insert(0,3)
# # using 0 will push forward all element , you can use append also but then use pop(0)
# print(queue)
# print(queue.pop())



# implementing queue by collections deque module

# from collections import deque

# d=deque()
# # use appendleft(element) to add values
# d.appendleft(1)
# d.appendleft(2)
# d.appendleft(3)
# print(d.pop())
# print(d.pop())




