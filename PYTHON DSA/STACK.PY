# ____________   STACK   _____________ #

# ways to implement stack is by using 1. list , 2. collections.deque , 3. queue.LifoQueue

'''

* linear ds
* follow LIFO order
* insertion and removal of element done at one end
* push operation -- for insrting element in stack
* pop  operation -- for removal of an element in stack
* example of stack is pile of coins , stack of books


'''

''' ___  functions associated with stack  __

* push(element)  -- add element into stack
* pop(element)   -- remove element from stack
* size()         -- gives length of stack
* top()          -- give reference of last element inserted into stack
* empty()        -- returns true if stack is empty 

'''

# stack implementation using list
# in list for push() operation it has append() which inserts the element

# stack = []  # creating empty stack 
# stack.append('x') # inserting element x into stack
# print(stack)
# print(type(stack))
# stack.pop() # removing element from stack
# print(stack)



# stack implementation using collection.deque
# for push() operation it has append()
# major benefit of using deque is that it has time complexity of O(1) as compared to list which has tc of O(n)
# from collections import deque

# stack = deque()
# stack.append(1)
# stack.append(2)
# stack.pop()
# print(stack)


# stack implementation using queue module

'''__ Functions available in queue __

* for printing element it does not have any function we need to use loop
* get()  -- remove element from queue
* maxsize() -- allowing queue to have the fixed maximum no of element to store
* empty() -- returns true if queue is empty else false
* full() -- if queue is full returns true
* put(element) -- insert element into queue
* qsize() -- gives size of a queue

'''

# from queue import LifoQueue

# stack = LifoQueue(maxsize=5) # creating empty stack
# stack.put(1)
# stack.put(2)
# stack.put(3)
# stack.put(3)
# stack.put(3)
# # print(stack.get())
# print(stack.full())
# print(stack.qsize())
# print(stack.empty())
