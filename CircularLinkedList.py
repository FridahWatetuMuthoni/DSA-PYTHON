#CircularLinked list => CIRCULARQUEUE
# Queue => FIRST IN , FIRST OUT : LAST IN LAST OUT
# new => append at the tail
# delete => remove from the front

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return f"<Node:{self.data}>"

class LinkedList:
    def __init__(self):
        self.tail = None
        self.count = 0
    
    def is_empty(self):
        return self.count == 0
    
    def __len__(self):
        return self.count
    
    def first(self):
        if self.is_empty():
            return "The queue is empty"
        head = self.tail.next
        return head.data
    
    def enqueue(self,data):
        node = Node(data)
        if(self.tail == None):
            self.tail = node
            node.next = node
        else:
            head = self.tail.next
            prev = self.tail
            prev.next = node
            node.next = head
            self.tail = node
            
        self.count += 1

    def dequeue(self):
        if(self.is_empty()):
            return 'The Queue is empty'
        head = self.tail.next
        if(self.count == 1):
            self.tail = None
        else:
            next = head.next
            self.tail.next = next
        self.count -= 1
        return head.data
    
    def rotate(self):
        if(self.size > 0):
            self.tail = self.tail.next
    
    def __repr__(self):
        if self.is_empty():
            return "The Queue is empty"
        nodes = []
        current = self.tail.next
        
        while True:
            if(current == self.tail.next):
                nodes.append(f"[Head:{current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next
            if(current == self.tail.next):
                break
        return " -> ".join(nodes)

cq = LinkedList()
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)
print(cq)
print(cq.first())
print(f"LinkedList Size:{cq.count}")
print(cq.dequeue())
print(cq)
print(cq.first())
print(f"LinkedList Size:{cq.count}")



