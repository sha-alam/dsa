def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            return mid
    # If we reach here, then the element was not present
    return -1


array = list(map(int, input("Enter an array: ").split()))
array.sort()
print("Your Array: ", array)
print("\nBinary Searching")
element = int(input("Enter the element: "))
result = binary_search(array, element)
if result != -1:
    print("Element is present at position", result+1)
else:
    print("Element is not present in array")
