class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return f"<Node:{self.data}>"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def is_empty(self):
        return self.head == None
    
    def __len__(self):
        return self.count
    
    def search(self,key):
        current = self.head
        index = 0
        while(current != None):
            if(current.data == key):
                return index
            current = current.next
            index += 1
        return None
    
    def clear_list(self):
        self.head = None
        self.tail = None
        self.count = 0
    
    def insert_at_head(self,data):
        node = Node(data)
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1
    
    def insert_at_tail(self,data):
        node  = Node(data)
        if(self.tail):
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.count += 1
    
    def insert_at_index(self,data,index):
        if(index < 0 or index > self.count):
            return 'Index is out of bound'
        if(index == 0):
            self.insert_at_head(data)
            return
        if(index == self.count):
            self.insert_at_tail(data)
            return
        
        node = Node(data)
        current = self.head
        #get the previous node to where you want to insert the new node
        for _ in range(index-1):
            current = current.next
        next = current.next
        node.next = next
        node.prev = current
        current.next = node
        if next != None:
            next.prev = node
        self.count += 1
    
    def delete_at_tail(self):
        if self.is_empty():
            return "No items to Delete"
        current = self.tail
        if(self.head == self.tail):
            self.head = None
            self.tail = None
        else:
            prev = current.prev
            prev.next = None
            self.tail = prev
        self.count -= 1
        return current
    
    def delete_at_head(self):
        if self.is_empty():
            return "No items to Delete"
        current = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = current.next
            self.head.prev = None
        self.count -= 1
        return current
    
    def delete_at_index(self,index):
        if self.is_empty():
            return "No items to Delete"
        if index > self.count or index < 0:
            return 'Index is out of bound'
        if index == 0:
            return self.delete_at_head()
        if index == self.count - 1:
            return self.delete_at_tail()
        
        current = self.head
        for _ in range(index):
            current = current.next
        
        prev_node = current.prev
        next_node = current.next
        prev_node.next = next_node
        if(next_node != None):
            next_node.prev = prev_node
        self.count -= 1
        return current
    
    
    def __repr__(self):
        if self.is_empty():
            return "The LinkedList is currently empty"
        
        nodes = []
        current = self.head
        
        while(current != None):
            if(current == self.head):
                nodes.append(f"[Head:{current.data}]")
            elif(current.next == None):
                nodes.append(f"[Tail:{current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next
        return " -> ".join(nodes)


ls = LinkedList()
ls.insert_at_head(1)
ls.insert_at_head(2)
ls.insert_at_head(3)
ls.insert_at_index(50, 1)
ls.insert_at_head(4)
ls.insert_at_tail(10)
ls.insert_at_tail(20)
ls.insert_at_tail(30)
ls.insert_at_head(5)
ls.insert_at_head(8)
ls.insert_at_tail(40)
ls.insert_at_tail(50)
ls.insert_at_tail(120)
ls.insert_at_index(45, 0)
ls.insert_at_index(40, 2)
ls.insert_at_index(70, 8)
ls.insert_at_index(250, 20)
ls.insert_at_index(89, 13)
ls.insert_at_index(9, 0)
print(ls.search(50))
print(ls)
print(ls.delete_at_tail())
print(ls.delete_at_head())
print(ls)
print(ls.delete_at_index(6))
print(ls)
ls.clear_list()
print(ls)

