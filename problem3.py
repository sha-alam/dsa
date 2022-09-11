# Author: MD.Shahdat Hossain Bhuian
def linear_search(arr,key):
    n=len(arr)
    for pos in range(n):
        if arr[pos]==key:
            return pos
    return -1


arr=list(map(int,input("Enter an array: ").split()))
print("Your array: ",arr)

print("\nLinear Search Start")
key=int(input("Enter the element: "))

result=linear_search(arr,key)
if result!=-1:
    print("Element is present at index: ",result)
else:
    print("Element is not present in array")
    
