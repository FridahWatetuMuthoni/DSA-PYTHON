x = {'data', 'structure', 'and', 'python'}

#Getting the length of a set
print(len(x))

#Checking if an element is in a set
print('structure' in x)

## SETS OPERATIONS
x1 = {'data', 'structure'}
x2 = {'python', 'java', 'c', 'data'}

## UNION OF SETS
union_set = x1.union(x2)
print(union_set)

## INTERSECTION OF SETS
intersection_set = x1.intersection(x2)
print(intersection_set)

##DIFFERENCE OF SETS
difference_sets_1 = x1.difference(x2)
difference_sets_2 = x2.difference(x1)
print(difference_sets_1)
print(difference_sets_2)

## SYMMETRIC DIFFERENCE
symmetric_difference_set = x1.symmetric_difference(x2)
print(symmetric_difference_set)

## SUBSET
is_subset_set = x1.issubset(x2)
print(is_subset_set)

## Immutable sets
"""
In Python, frozenset is another built-in type data structure, which is, in all respects, exactly 
like a set, except that it is immutable, and so cannot be changed after creation. The order of the 
elements is also undefined. A frozenset is created by using the built-in function frozenset():
"""
x = frozenset(['data', 'structure', 'and', 'python'])
print(x) #returns frozenset({'python', 'structure', 'data', 'and'})

