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

## BINARY TREE
A binary tree is where each node have at most 2 descendants
A binary tree has two main components a node and a root
A node with no children is called a leaf node
Trees are hierarchical data structures
Array, Linked list, stack, queue are linear data structures
The height of a node is the number of edges on the longest path between that node and a leaf
A binary tree can either be balanced or unbalanced.
In a balance tree the difference in height of the left and right subtree of every node should not be greater than one.
An unbalanced binary tree is a binary tree that has a difference of more than 1 between the right 
subtree and left subtree.

### Binary Tree Rules
1. Has at most two children
2. Exactly one root
3. exactly 1 path between root and any node

### Binary Tree Terminology
1. Node: Each circled letter in the preceding diagram represents a node. A node is any data structure that stores data.
2. Root node: The root node is the first node from which all other nodes in the tree descend from. In other words, a root node is a node that does not have a parent node. In every tree, there is always one unique root node. The root node is node A in the above example tree.
3. Subtree: A subtree is a tree whose nodes descend from some other tree. For example, nodes F, K, and L form a subtree of the original tree.
4. Degree: The total number of children of a given node is called the degree of the node. A tree consisting of only one node has a degree of 0. The degree of node A in the preceding diagram is 2, the degree of node B is 3, the degree of node C is 3, and, the degree of node G is 1.
5. Leaf node: The leaf node does not have any children and is the terminal node of the given tree. The degree of the leaf node is always 0. In the preceding diagram, the nodes J, E, K, L, H, M, and I are all leaf nodes.
6. Edge: The connection among any given two nodes in the tree is called an edge. The total number of edges in a given tree will be a maximum of one less than the total nodes in the tree. An example edge is shown in Figure 6.1.
7. Parent: A node that has a subtree is the parent node of that subtree. For example, node B is the parent of nodes D, E, and F, and node F is the parent of nodes K and L.
8. Child: This is a node that is descendant from a parent node. For example, nodes B and C are children of parent node A, while nodes H, G, and I are the children of parent node C. 
9. Sibling: All nodes with the same parent node are siblings. For example, node B is the sibling of node C, and, similarly, nodes D, E, and F are also siblings. 
10. Level: The root node of the tree is considered to be at level 0. The children of the root node are considered to be at level 1, and the children of the nodes at level 1 are considered to be at level 2, and so on. For example, in Figure 6.1, root node A is at level 0, nodes B and C are at level 1, and nodes D, E, F, H, G, and I are at level 2.
11. Height of a tree: The total number of nodes in the longest path of the tree is the height of the tree. For example, in Figure 6.1, the height of the tree is 4, as the longest paths, A-B-D-J, A-C-G-M, and A-B-F-K, all have a total number of four nodes each.
12. Depth: The depth of a node is the number of edges from the root of the tree to that node. In the preceding tree example, the depth of node H is 2.


























### Types of Binary Trees
1. Full Binary Tree = a full binary tree is where each node either has two descendants or no descendants
2. Complete Binary Tree = is when each node has two descendants

### Binary Search Insertion Rules
1. First step is to select a root
2. When the next value is greater than root go rigth else go left
3. If you have a repeated value, put it to the right or left

Example:
arr = [8,3,10,1,6,14,4]
1. Make the first element of the array the root
2. The next value is 3. 3 is less than 8 so we place it left
3. The next value is 10. 10 is greater than 8 so we place it right
4. The next value is 1. 1 is less than 8 so we go left. 1 is less than 3 so we place is left
5. The next value is 6. 6 is less than 8 so we go left.6 is greater than 3 so we place it right
6. The next value is 14. 14 is greater than 8 so we go right. 14 is greater than 10 so we place it right
7. The next value is 4. 4 is less than 8 so we go left. 4 is greater than 3 so we go right. 4 is less than 6 so we place it left.

### Binary Search Algorithms

1. Breadth First Search -> uses a queue -> FIFO
2. Breadth First Search -> uses a stack -> LIFO