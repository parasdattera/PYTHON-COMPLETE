'''      ________ BINARY SEARCH TREE ________

# binary search tree is binary tree with additional restriction.

# Restriction is : 
    1. left child must always be less than root node.
    2. right child must always be greater than root node.

# benefits : insertion , deletion , search is more efficient then binary tree.

# applications : best for hierarchical data having values less or greater then each other

# methods : insert element into bst , delete element from bst , search element into bst

'''

# implementation



# implementing binary search tree , creating class for creating node and methods

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def add_child(self,data):
        if self.data == data:
            return # node already exist
        if data<self.data:
            #if root has left sub tree then traverse to left otherwise insert at self.left
            if self.left:
                #traverse into left subtree
                self.left.add_child(data)
            else:
                #insert/build subtree into left of root
                self.left= Node(data)        
        else:
             #if root has right sub tree then traverse to right otherwise insert at self.right
            if self.right:
                #traverse into right subtree
                self.right.add_child(data)
            else:
                #insert/build subtree into right of root
                self.right= Node(data)
    
    def in_order_traversal(self):
        # creating empty list for storing tree values in inorder traversal
        elements = []
        # inserting recursively left elements from tree
        if self.left:
            elements+=self.left.in_order_traversal()
        # inserting root value from tree
        elements.append(self.data)
        # inserting recursively right elements from tree
        if self.right:
            elements+=self.right.in_order_traversal()
        return elements

    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if self.data:
            if self.left:
                return self.left.find_min()
        return self.data

    def find_max(self):
        if self.data:
            if self.right:
                return self.right.find_max()
        return self.data
    
    
    
    def Calculate_Sum(self):
        sum=0
        if self.data:
            sum+=self.data
            if self.left:
                sum+= self.left.Calculate_Sum()
            if self.right:
                sum+= self.right.Calculate_Sum()
        return sum
    
    def PostOrderTraversal(self):
        elements = []
        if self.left:
            elements+=self.left.PostOrderTraversal()
        if self.right:
            elements+=self.right.PostOrderTraversal()
        elements.append(self.data)
        return elements
    
    def PreOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements+=self.left.PreOrderTraversal()
        if self.right:
            elements+=self.right.PreOrderTraversal()
        return elements
        
    





def Build_Tree(elements):
        print("Building tree with : ",elements)
        root=Node(elements[0])
        
        for i in range(1,len(elements)):
            root.add_child(elements[i])
        
        return root    



if __name__ == '__main__':
    numbers=[5,2,4,6,9,8,7]
    root=Build_Tree(numbers)
    print(root.PreOrderTraversal())

    pass
    

# if __name__=='__main__':
#     countries = ["India","Pakistan","Germany","USA","China","India","UK","USA"]
#     country_tree=Build_Tree(countries)
#     print(country_tree.in_order_traversal())
#     print(country_tree.search("India"))
    
    