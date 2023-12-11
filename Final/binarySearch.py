def binarySearch(searchList,searchNumber):
    low = 0; high = len(searchList) - 1
    mid = 0

    while low <= high:
        mid = (low+high)//2
        if searchList[mid] < searchNumber:
            low = mid + 1
        elif searchList[mid] > searchNumber:
            high = mid - 1
        else:
            return mid
    return -1

arr = [ 2, 3, 4, 5, 10, 40, 86, 100 ]
x = 4

def binaryRecursiveSearch(searchList,low,high,searchNumber):
    #base case
    if low > high:
        return -1
    
    #set midpoint from low and high
    mid = (low+high)//2

    if searchList[mid] < searchNumber: #set low to mid+1
        return binaryRecursiveSearch(searchList,mid+1,high,searchNumber)
    elif searchList[mid] > searchNumber: #set high to mid-1
        return binaryRecursiveSearch(searchList,low,mid-1,searchNumber)
    else:
        return mid

# Function call
result = binaryRecursiveSearch(arr, 0,len(arr)-1,x)

if result != -1:
    print("Element is present at index", str(result))
    print(f"Element is: {str(arr[result])}")
else:
    print("Element is not present in array")