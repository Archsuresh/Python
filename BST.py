class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            
