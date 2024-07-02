def binary_search(arr, target):
    start = 0
    end = len(arr)
    
    while(start < end):
        mid = (start + end) // 2
        
        if(arr[mid] == target):
            return True
        elif(arr[mid] < target):
            start = mid + 1
        else:
            end = mid 
    return False

arr = [5, 7,9, 10, 12, 15, 17, 18, 20, 15, 28, 30, 34, 37, 39, 40, 42, 44, 46, 50, 52, 65, 69, 72, 80, 85,88,90,94,96,100]
result = binary_search(arr,940)

if(result):
    print('Number found')
else:
    print('Number not found')