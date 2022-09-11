def linear_search(arr, key):
    n = len(arr)
    for pos in range(n):
        if arr[pos] == key:
            return pos
    return -1


array = list(map(int, input("Enter an array: ").split()))
print("Your array: ", array)

print("\nLinear Search Start")
element = int(input("Enter the element: "))

result = linear_search(array, element)
if result != -1:
    print("Element is present at position: ", result+1)
else:
    print("Element is not present in array")
