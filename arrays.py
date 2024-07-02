new_list = [1, 2, 3, 4, 5, 6]

#accessing values from an array -> O(1) -> due to pointer arithmetic
print(new_list[0])

# Searching for values: sorted->binary search -> O(log n)
# Searching for values: unsorted->linear search -> O(n)
for num in new_list: #O(n)
    if(num == 5):
        print(True)

# Inserting at a random index O(n)
# Inserting at the end of an array O(1)
# The list growth pattern in python is 0,4,8,16,25,35,46
# Deleting at the end of the list O(1)
# Deleting at any random index O(n)