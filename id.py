def ins(arr,pos,n):
    arr.insert(pos,n)

def dele(arr,pos):
    arr.remove(arr[pos])

arr=[1,2,3,4,5,6]
ins(arr,2,8)
print(arr)
dele(arr,5)
print(arr)