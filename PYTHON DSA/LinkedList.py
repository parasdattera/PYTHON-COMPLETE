'''
_____   Linked List  _____

*  collection or group of nodes

*  each node contains data and reference(pointer) which contains the address of next node.

*  linear DS

*  element stored randomly in memory 

'''


# Singly Linked List


#implementation using user defined classes

#traversing in linked list
# Node creation , sll creationg , traversing , inserting in linked list

# Node creation , sll creationg , traversing , inserting in linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class Sll:
#     def __init__(self):
#         self.head = None
    
#     def Traversal(self):
#         if self.head is None:
#             print("Singly Linked List is empty! ")
#         else:
#             a = self.head
#             while a is not None:
#                 print(a.data,end=" ")
#                 a = a.next
    
#     def InsertItemAtBeginning(self,data):
#         NewNode=Node(data)
#         NewNode.next=self.head
#         self.head=NewNode
    
#     def InsertItemAtEnd(self,data):
#         NewNode=Node(data)
#         a = self.head
#         while a.next is not None:
#             a = a.next
#         a.next = NewNode
        
#     def InsertItemAtSpecificPos(self,data,pos):
#         NewNode=Node(data)
#         a = self.head
#         for i in range(1,pos-1):
#             a = a.next
#         NewNode.next = a.next
#         a.next=NewNode
    
#     def DeletionAtBeginning(self):
#         a = self.head
#         self.head = a.next
#         a.next = None
        
#     def DeletionAtEnd(self):
#         previous = self.head
#         a = self.head.next
#         while a.next is not None:
#             a = a.next
#             previous = previous.next
#         previous.next = None
        
#     def DeletionAtSpecifiedPosition(self,pos):
#         previous = self.head
#         a = self.head.next
#         for i in range(1,pos-1):
#             a = a.next
#             previous = previous.next
#         previous.next = a.next
#         a.next = None
    

# n1=Node(1)
# sll=Sll()
# sll.head=n1
# n2=Node(2)
# n1.next=n2
# n3=Node(3)
# n2.next=n3
# n4=Node(4)
# n3.next=n4
# sll.Traversal()
# print()
# sll.InsertItemAtBeginning(0)
# sll.Traversal()
# print()
# sll.InsertItemAtEnd(5)
# sll.Traversal()
# sll.InsertItemAtSpecificPos(6,7)
# print()
# sll.Traversal()
# print()
# sll.DeletionAtBeginning()
# sll.Traversal()
# print()
# sll.DeletionAtEnd()
# sll.Traversal()
# print()
# sll.DeletionAtSpecifiedPosition(3)
# sll.Traversal()






 # Doubly Linked List

 # Doubly Linked List

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class Dll:
#     def __init__(self):
#         self.head = None
        
        
#     def DeletionAtSpecifiedPos(self,pos):
#         b=self.head
#         a=self.head.next
#         for i in range(1,pos-1):
#             a=a.next            
#             b=b.next
#         b.next=a.next
#         a.next.prev=b
#         a.next=None
#         a.prev=None
        
    
#     def DeletionAtEnd(self):
#         a = self.head.next
#         before=self.head
#         while a.next is not None:
#             a=a.next
#             before=before.next
#         before.next=None
#         a.prev=None
        
        
#     def DeletionAtBeginning(self):
#         a=self.head
#         self.head=a.next
#         a.next=None
#         self.head.prev=None
        
#     def InsertionAtSpecifiedPos(self,data,pos):
#         newNode= Node(data)
#         a=self.head
#         for i in range(1,pos-1):
#             a=a.next
#         newNode.prev=a
#         newNode.next=a.next
#         a.next=newNode
        
        
            
        
        
        
#     def InsertionAtBeginning(self,data):
#         newNode=Node(data)
#         a=self.head
#         a.prev=newNode
#         newNode.next=a
#         self.head=newNode
        
#     def InsertionAtEnd(self,data):
#         newNode=Node(data)
#         a=self.head
#         while a.next is not None:
#             a=a.next
#         a.next=newNode
#         newNode.prev=a
        
        
        
#     def ForwardTraversal(self):
#         if self.head is None:
#             print(" DLL is empty !")
#         else:
#             a=self.head
#             while a is not None:
#                 print(a.data,end=" ")
#                 a=a.next
                
                
#     def BackwardTraversal(self):
#         if self.head is None:
#             print(" DLL is empty !")
#         else:
#             a=self.head
#             while a.next is not None:
#                 a=a.next
#             while a is not None:
#                 print(a.data,end=" ")
#                 a=a.prev
                
    
                
    
    
# n1=Node(1)
# dll=Dll()
# dll.head=n1
# n2=Node(2)
# n1.next=n2
# n2.prev=n1
# n3=Node(3)
# n2.next=n3
# n3.prev=n2
# n4=Node(4)
# n3.next=n4
# n4.prev=n3
# dll.ForwardTraversal()
# print()
# dll.BackwardTraversal()
# print()
# dll.InsertionAtBeginning(0)
# dll.ForwardTraversal()
# print()
# dll.BackwardTraversal()
# print()
# dll.InsertionAtEnd("hello")
# dll.ForwardTraversal()
# print()
# dll.InsertionAtSpecifiedPos("paras",3)
# dll.ForwardTraversal()
# print()
# dll.DeletionAtBeginning()
# dll.ForwardTraversal()
# print()
# dll.DeletionAtEnd()
# dll.ForwardTraversal()
# print()
# dll.DeletionAtSpecifiedPos(3)
# dll.ForwardTraversal()

 




 # Circular Linked List

'''
main difference in cll is that last node of cll does not have next/referenced value to None instead 
it has address value of first node creating a circle of linked list

it can be of two types 

1. Singly Circular Linked List (same as sll)
2. Doubly Circular Linked List (same as dll)


'''