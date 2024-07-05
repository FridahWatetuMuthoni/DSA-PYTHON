class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"<Node->Data:{self.data}->Left:{self.left}->Right:{self.right}"


class BST:
    def __init__(self,data):
        self.root = Node(data)
        self.count = 1
    
    def __len__(self):
        return self.count
    
    def is_empty(self):
        return len(self.count) == 0
    
    def insert_recur(self, data):
        new_node = Node(data)
         
        def traverse(node):
            if(data > node.data):
                if(node.right is not None):
                    traverse(node.right)
                else:
                    node.right = new_node
            else:
                if(node.left is not None):
                    traverse(node.left)
                else:
                    node.left = new_node
        traverse(self.root)
    
    
    def insert_iter(self,data):
        new_node = Node(data)
        current = self.root
        
        while(True):
            if(data > current.data):
                #go right
                if(current.right is not None):
                    current = current.right
                else:
                    current.right = new_node
                    return self.root
            else:
                #go left
                if(current.left is not None):
                    current = current.left
                else:
                    current.left = new_node
                    return self.root
    
    def max(self):
        if(self.is_empty()):
            return 'The tree is empty'
        current = self.root
        
        while(current.right != None):
            current = current.right
        return current.data
    
    def min(self):
        if(self.is_empty()):
            return 'The tree is empty'
        current = self.root
        
        while(current.left != None):
            current = current.left
        return current.data
    
    def search_number(self,num):
        current = self.root
        if(self.is_empty()):
            return 'The Tree is empty'
        while(current.left != None or current.right != None):
            if(current.data == num):
                return True
            if(num > current.data):
                current = current.right
            else:
                current = current.left
        return False
    
    def search_string(self, str):
        if(self.is_empty()):
            return 'The tree is empty'
        current = self.root
        
        def search(node):
            if(node.data == str):
                return True
            if(node.left is not None):
                search(node.left)
            if(node.right is not None):
                search(node.right)
        search(current)
        return False
    
    def get_node_with_parent(self,data):
        parent = None
        current = self.root
        
        while current is not None:
            if(current.data == data):
                return (parent,current)
            elif(current.data > data):
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right
        return (parent,None)
    
    def delete_node(self,data):
        # if it has no children just remove it
        # if it has one child, we swap the value of that node with its child, and then delete the node
        # if it has two children, we first find the in-order successor or predecessor, swap their values, and then delete that node
        parent,node = self.get_node_with_parent(data)
        
        if(parent is None and node is None):
            return False
        
        children_count = 0
        
        if node.left and node.right:
            children_count = 2
        elif node.left is None and node.right is None:
            children_count = 0
        else:
            children_count = 1
            
        if(children_count == 0):
            if parent:
                if parent.right is node:
                    parent.right = None
                else:
                    parent.left = None
            else:
                self.root = None
        elif children_count == 1:
            next_node = None
            if(node.left):
                next_node = node.left
            else:
                next_node = node.right
            
            if parent:
                if parent.left is node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.root = None
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left
            
            node.data = leftmost_node.data

        
    def df(self):
        if(self.is_empty()):
            return 'The tree is empty'
        results = []
        stack = [] #Last In , Last Out-> append and pop
        stack.push(self.root)
        while(len(stack) > 0):
            current = stack.pop()
            results.push(current.data)
            if(current.left is not None):
                stack.push(current.left)
            if(current.right is not None):
                stack.push(current.right)
        return results
    
    def bf(self):
        if(self.is_empty()):
            return 'The tree is empty'
        results = []
        queue = [] #First In , First Out append,
        queue.push(self.root)
        while(len(queue) > 0):
            current = queue.pop(0)
            results.append(current.data)
            if(current.left is not None):
                queue.append(current.left)
            if(current.right is not None):
                queue.append(current.right)
        return results
    
    def inorderDF(self):
        if(self.is_empty()):
            return 'The tree is empty'
        # LROOTR
        results = []
        def traverse_tree(node):
            if(node.left is not None):
                traverse_tree(node.left)
            results.append(node.data)
            if(node.right is not None):
                traverse_tree(node.right)
    
    def preorderDF(self):
        if(self.is_empty()):
            return 'The tree is empty'
        # ROOTLR
        results = []
        def traverse_tree(node):
            results.append(node.data)
            if(node.left is not None):
                traverse_tree(node.left)
            if(node.right):
                traverse_tree(node.right)
    
    def postorderDF(self):
        if(self.is_empty()):
            return 'The tree is empty'
        # LRROOT
        results = []
        def traverse_tree(node):
            if(node.left is not None):
                traverse_tree(node.left)
            if(node.right is not None):
                traverse_tree(node.right)
            results.append(node.data)


#ROOTLR
def preOrderDF(node,results=[]):
    if(node is None):
        return results
    results.push(node.data)
    preOrderDF(node.left)
    preOrderDF(node.right)
    
#LRROOT
def postOrderDF(node,results=[]):
    if(node is None):
        return results
    postOrderDF(node.left)
    postOrderDF(node.right)
    results.push(node.data)
    
#LROOTR 
def inOrderDF(node,results=[]):
    if(node is None):
        return results
    inOrderDF(node.left)
    results.push(node.data)
    inOrderDF(node.right)


def get_node(root,data):
    current = root
    parent = None
    while(current is not None):
        if(current.data == data):
            return(parent,current )
        elif(data < current.data):
            parent = current
            current = current.left
        else:
            parent = current
            current  = current.right
    return(None,None)

def find_minimum(node):
    current = node
    while(current.left != None):
        current = current.left
    return current

def delete_node(root,data):
    parent, node = get_node(root,data)
    
    if(node is None):
        return False
    
    number_of_children = 0
    if(node.left and node.right):
        number_of_children = 2
    elif(node.left is None and node.right is None):
        number_of_children = 0
    else:
        number_of_children = 1
    
    
    if(number_of_children == 0):
        if(parent is None):
            return None
        if(parent.left == node):
            parent.left = None
        else:
            parent.right = None
            
    elif(number_of_children == 1):
        if(parent is None):
            return None
        if(parent.left == node):
            parent.left = node.left if node.left else node.right
        else:
            parent.right = node.right if node.right else node.left
    else:
        # find the smallest value on the right side and replace the root with it
        # OR
        # find the largest value on the left size and replace the root with it
        # The value gotten from either of the above will either has one child or its a leaf
        successor_node = find_minimum(node.right)
        node.data = successor_node.data
        node.right = delete_node(node.right, successor_node.data)
        