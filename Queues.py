class Queue:
    def __init__(self):
        self.collection = []
    
    def print_collection(self):
        print(self.collection)
    
    def is_empty(self):
        return len(self.collection) == 0
    
    def enqueue(self, element):
        self.collection.append(element)
    
    def dequeue(self):
        if(self.is_empty()):
            return 'The Queue is empty'
        self.collection.remove(self.collection[0])

    
    def front(self):
        return self.collection[0]
    
    def size(self):
        return len(self.collection)



# queque =  Queue()
# queque.enqueue(1)
# queque.enqueue(2)
# queque.enqueue(3)
# queque.enqueue(4)
# queque.enqueue(5)
# queque.enqueue(6)

# queque.print_collection()
# print(queque.dequeue())
# queque.print_collection()
# print(queque.front())
# print(queque.size())


class PriolityQueue:
    def __init__(self):
        self.collection = []
    
    def print_collection(self):
        print(self.collection)
    
    def is_empty(self):
        return len(self.collection) == 0
    
    def enqueue(self, element):
        if(self.is_empty()):
            self.collection.append(element)
        else:
            added = False
            for i in range(0, len(self.collection)):
                if(element[1] < self.collection[i][1]):
                    self.collection.insert(i,element)
                    added = True
                    break
            if(added == False):
                self.collection.append(element)
    
    def dequeue(self):
        if(self.is_empty()):
            return 'The Queue is empty'
        self.collection.remove(self.collection[0])
    
    def front(self):
        return self.collection[0]
    
    def size(self):
        return len(self.collection)


pq = PriolityQueue()
pq.enqueue(['Beau Carnes',2])
pq.enqueue(['Quincy Larson',3])
pq.enqueue(['Ewa Sandy',1])
pq.enqueue(['Briana Swift',2])
pq.print_collection()
print(pq.front())
pq.dequeue()
pq.print_collection()