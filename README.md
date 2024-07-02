# Data Structures and Algorithms

## Algorithms

An algorithm is a set of steps a program takes to finish a task.
An algorithm has to have a clearly defined problem statement, input and output.
The steps in an algorithm need to be in a very specific order.
The steps also need to be distinct.
The algotirhm should produce a result.
The algorithm should complete in a finite amount of time.

## Space and Time Complexity

Space and Time Complexity is basically how the algorithm slows down as data increases

## Data Structures
Data Structure is a data storage format. It is the collection of values and the format they are stored in, the relationships
between the values in the collection as well as the operations applied on the data stored in the structure.

## Data Structures Operations
1. Inserting Data -> Insert
2. Searching Data -> Search
3. Accessing Data -> Access
4. Deleting Data -> Delete

## Arrays
An array is a collection of data items. An array is stored in contiguous memory locations.
inserting-> O(n)
Searching-> O(n)
Accessing-> O(1)
Deleting-> O(n)

```python

new_list = [1, 2, 3, 4, 5, 6]

```

Accessing values from an array -> O(1) -> due to pointer arithmetic

```python 
print(new_list[0])
```

Searching for values: sorted->binary search -> O(log n)
Searching for values: unsorted->linear search -> O(n)

```python

for num in new_list: #O(n)
    if(num == 5):
        print(True)
```

Inserting at a random index O(n)
Inserting at the end of an array O(1)
The list growth pattern in python is 0,4,8,16,25,35,46
Deleting at the end of the list O(1)
Deleting at any random index O(n)

## SETS
A set is an unordered collection of hashable objects. It is iterable, mutable, and has unique elements. 
The order of the elements is also not defined. While the addition and removal of items are allowed, the items themselves within the set must be immutable and hashable. Sets support membership testing operators (in, not in), and operations such as intersection, union, difference, and symmetric difference. Sets cannot contain duplicate items. They are created by using the built-in set() function or curly braces {}. A set() returns a set object from an iterable. For example:

```python
x1 = set(['and', 'python', 'data', 'structure'])
print(x1)
x2 = {'and', 'python', 'data', 'structure'}
print(x2)
```

### SETS OPERATIONS

#### SETS UNION
Union of two sets is when you combine items from set A and set B to create a
set of unique elements

```python
x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

union_set = x1.union(x2)
print(union_set) ## returns {'data', 'structure','python', 'java', 'c'}

```

#### SETS INTERSECTION
The intersection of two sets returns a set that contains the items that are both
in set A nad set B

```python
x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

intersection_set = x1.intersection(x2)
print(intersection_set) ## returns {'data'}

```

#### SETS DIFFERENCE
The difference between two sets returns all the elements that are in set A but not in set B


```python
x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

difference_sets_1 = x1.difference(x2)
difference_sets_2 = x2.difference(x1)

print(difference_sets_1) ## returns {'structure'}
print(difference_sets_2) ## returns {'python','java','c'}

```

#### SETS SYMMETRIC DIFFERENCE
The symmetric difference returns all items that are in set A ot set B but not both


```python
x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

symmetric_difference_set = x1.symmetric_difference(x2)
print(symmetric_difference_set) ## returns {'structure','python','java','c'}

```


## STACKS
A stack is a data structure that stores data, similar to a stack of plates in a kitchen. You can put 
a plate on the top of the stack, and when you need a plate, you take it from the top of the stack. 
The last plate that was added to the stack will be the first to be picked up from the stack:
Stacks uses the Last In , First Out principle or First In , Last Out principle.
A good use case is the browser history
We use the push method to add to the end of the stack and the pop method to remove from the end of the stack and peek is used to display the top element of a stack.

### STACKS OPERATIONS

#### PUSH
push is used to place data to a stack

#### POP
pop is used to remove the top element of a stack

#### PEEK
peek is used to display the top element of a stack

## QUEUES

The queue data structure is very similar to the regular queue you are accustomed to in real life. It is just like a line of people waiting to be served in sequential order at a shop. Queues are a fundamentally important concept to grasp since many other data structures are built on them.
A queue works as follows. The first person to join the queue usually gets served first, and everyone will be served in the order in which they joined the queue. The acronym FIFO best explains the concept of a queue. FIFO stands for first in, first out.
Therefore, people are dequeued from the front of the queue and enqueued from the back where they wait their turn. 
The operation to add an element to the queue is known as enqueue. Deleting an element from the queue uses the dequeue operation. Whenever an element is enqueued, the length or size of the 
queue increments by 1, and dequeuing an item reduces the number of elements in the queue by 1. 


### QUEUES OPERATIONS

#### ENQUEUE
elements are added at the end of the queue

#### DEQUEUE
elements are removed from the front of the queue

#### FRONT
front is used to display the first element of the queue

## Priority Queues
In the course of normal queue operations, when an element is removed from a queue,that element is always the first element that was inserted into the queue. There are certain applications of queues, however, that require that elements be removed in an order other than first-in, first-out. When we need to simulate such an application, we need to create a data structure called a priority queue.
A priority queue is one where elements are removed from the queue based on a priority constraint. For example, the waiting room at a hospital’s emergency department (ED) operates using a priority queue. When a patient enters the ED, he or she is seen by a
triage nurse. This nurse’s job is to assess the severity of the patient’s condition and assign the patient a priorty code. Patients with a high priority code are seen before patients
with a lower priority code, and patients that have the same priority code are seen on a first-come, first-served, or first-in, first-out, basis.

## LINKED LISTS
A linked list is a data structure where the data elements are stored in a linear order. Linked lists provide efficient storage of data in linear order through pointer structures. Pointers are used to store the memory address of data items. They store the data and location, and the location stores the position of the next data item in the memory.
Each node contains two parts the data and the pointer which points to the next node.
Types Of Linked Lists
1. Singly linked lists -> each node stores a pointer to the next node
2. Doubly linked lists -> each node stores a pointer to the next node and the previous node
3. Circular lists -> a circular list is when the last/tail node doent point to none but it instead points to the head node

The first Node in a linked list is called the head while the last Node is called a tail.
The tail doesnt point to anything.
