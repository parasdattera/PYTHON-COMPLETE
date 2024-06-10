'''        _____  BINARY TREE  ____

* Hiererchical Data Structure
* Topmost element is root of tree
* Every node can have at most 2 children nodes
* Can't access elements randomly using index
* example -- file system hierarchy 

* Traversal Methods/Functions -- 
        1. preorder(root)        : root - left - right
        2. postorder(root)       : left - right - root
        3. inorder(root)         : left - root - right

        

'''


# implementing using 3rd party modules

# from binarytree import build, Node

# root = build([1,2,3,4,5,6,7,8,9])
# print(root)


# implementing using creating user defined classes and methods

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def TraversalPreorder(self):
        print(self.data,end=" ")
        if self.left:
            self.left.TraversalPreorder()
        if self.right:
            self.right.TraversalPreorder()
    
    def TraversalPostorder(self):
        if self.left:
            self.left.TraversalPostorder()
        if self.right:
            self.right.TraversalPostorder()
        print(self.data,end=" ")
    
    def TraversalInorder(self):
        if self.left:
            self.left.TraversalInorder()
        print(self.data,end=" ")
        if self.right:
            self.right.TraversalInorder()
            
    

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.left=Node(6)
root.right.right=Node(7)

print("Preorder traversal : ", end=" ")
root.TraversalPreorder()
print()
print("Postorder traversal : ", end=" ")
root.TraversalPostorder()
print()
print("Inorder traversal : ", end=" ")
root.TraversalInorder()
        
        
        


