# Author: MD.Shahdat Hossain Bhuian
arr=list(map(int,input("Enter an Array: ").split()))
print("Your Array: ",arr)

print("\nInsertion Operation")
ele=int(input("Enter an element: "))
pos=int(input("Enter the position: "))
arr.insert(pos-1,ele)
print("After insertion: ",arr)

print("\nDeletion Operation")
pos=int(input("Enter a position to delete an element: "))
arr.remove(arr[pos-1])
print("After deletion your array: ",arr)
