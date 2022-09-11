## Author: MD.Shahdat Hossain Bhuian

def binary_search(arr, low, high, key):
	if high >= low:
		mid = (high + low) // 2
		if arr[mid] == key:
			return mid
		elif arr[mid] > key:
			return binary_search(arr, low, mid - 1, key)
		else:
			return binary_search(arr, mid + 1, high, key)
	else:
		return -1

arr=list(map(int,input("Enter an array: ").split()))
print("Your Array: ",arr)

print("\nBinary Searching")
key=int(input("Enter the element: "))

result = binary_search(arr, 0, len(arr)-1, key)
if result!=-1:
	print("Element is present at index", result)
else:
	print("Element is not present in array")
