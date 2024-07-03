class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return f"< Node data: {self.data} >"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        """if the head is None it means that the linked list is empty"""
        return self.head == None
    
    def length(self):
        """ 
        The method visits each node in the linked list to determine the size of it.
        The method has a time complexity of O(n) because we need to traverse thru all the nodes.
        """
        current = self.head
        count = 0
        while(current != None):
            count += 1
            current = current.next
        return count
    
    def search(self,key):
        """ the operation takes O(n) """
        current = self.head
        index = 0
        while(current != None):
            if(current.data == key):
                return index
            current = current.next
            index += 1
        return None
    
    def total(self):
        total = 0
        current = self.head
        while(current != None):
            total += current.data
            current = current.next
        return total

    def insert_at_head(self,data):
        """
        When we insert at the head of the linkedlist the operation is O(1)
        When we are inserting at the head we are basically replacing the current head with the new created node
        """
        node = Node(data)
        node.next = self.head
        self.head = node
        if(self.tail is None):
            self.tail = node
    
    def insert_at_tail(self,data):
        """
        When we insert at the end of the linkedlist the operation is O(1)
        When we are inserting at the tail we are basically replacing the current tail with the new created node
        """
        node = Node(data)
        if(self.tail):
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
            
    
    def insert_at_index(self,data,index):
        """"""
        if(index == 0):
            self.insert_at_head(data)
            return
            
        count = 0
        current = self.head
        node = Node(data)
        
        while(current != None):
            if(index == count + 1):
                node.next = current.next
                current.next = node
                if(node.next is None):
                    self.tail = node
                return
            count += 1
            current = current.next
        if(index > count):
            print('Index is out of Bound')
            return 'Index is out of Bound'

    def delete_at_head(self):
        """it takes O(1)"""
        if self.is_empty():
            return "No items to Delete"
        deleted_item = self.head
        self.head = self.head.next
        if(self.head == None):
            self.tail = None
        return deleted_item
    
    def delete_at_tail(self):
        """it takes O(n)"""
        if self.is_empty():
            return "No items to Delete"
        current = self.head
        if current.next == None:
            deleted_item = current
            self.head = None
            self.tail = None
            return deleted_item
        while current.next.next != None:
            current = current.next
        deleted_item = current.next
        current.next = None
        self.tail = current
        return deleted_item
    
    def delete_at_index(self,index):
        """it takes O(n)"""
        if self.is_empty():
            return "No items to Delete"
        if index == 0:
            return self.delete_at_head()
        
        count  = 0
        current = self.head
        prev = self.head
        deleted_item = self.head
        
        while current != None and count < index -1:
            count += 1
            current = current.next
        
        if current != None and current.next == None:
            print('Index is Out of Bound')
            return "Index is out of Bound"
        deleted_item = current.next
        current.next = current.next.next
        if current.next is None:
            self.tail = current
        return deleted_item
        
    def clear_list(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        """
        Returns the string representation of the LinkedList
        It takes O(n)
        """
        if self.is_empty():
            return "The LinkedList is currently empty"
        current = self.head
        nodes = []
        
        while(current != None):
            if(current is self.head):
                nodes.append(f"[Head: {current.data}]")
            elif(current.next == None):
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next
        return " -> ".join(nodes)

ls = LinkedList()
ls.insert_at_head(1)
ls.insert_at_head(2)
ls.insert_at_head(3)
ls.insert_at_head(4)
ls.insert_at_head(5)
ls.insert_at_tail(10)
ls.insert_at_tail(20)
ls.insert_at_tail(30)
ls.insert_at_tail(40)
ls.insert_at_tail(50)
ls.insert_at_head(8)
ls.insert_at_index(58, 5)
ls.insert_at_index(70, 8)
ls.insert_at_index(250, 20)
ls.insert_at_index(89, 13)
ls.insert_at_index(9, 0)
print(ls.search(250))
print(ls)
print(ls.total())
print(ls.delete_at_tail())
print(ls.delete_at_head())
print(ls.delete_at_index(6))
print(ls)
ls.clear_list()
print(ls)
