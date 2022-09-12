def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
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
