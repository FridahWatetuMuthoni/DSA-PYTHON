## using the list data structure to create a stack data structure
def palindrome_checker(word):
    letters = []
    rword = ''
    
    for letter in word:
        letters.append(letter)
        
    while letters:
        rword += letters.pop()
    
    if(rword == word):
        print(f"{word} is a palidrome")
    else:
        print(f"{word} is not a palidrome")

palindrome_checker('jane')

## using classes to create a stack data structure

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self,element):
        self.items.append(element)
    
    def pop(self):
        if(self.isEmpty()):
            return 'underFlow'
        return self.items.pop()
    
    def peek(self):
        if(self.isEmpty()):
            return "No itmes in the Stack"
        return self.items[len(self.items) - 1]
    
    def printStack(self):
        str = ""
        for item in self.items:
            str += f"{item} "
        return str.strip()

stack  =  Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.printStack())
print(stack.pop())
print(stack.peek())
print(stack.printStack())


# Stack implementation using linked lists
