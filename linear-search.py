def linear_search(target, arr):
    for element in arr:
        if(element ==target):
            return 'Element Found'
            
    return 'Element Was not Found'


numbers = [12, 87, 98, 78, 63, 68, 45, 12, 1, 56]
print(linear_search(56,numbers)) # O(n) => linear time complexity