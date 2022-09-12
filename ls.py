def ls(arr,x):
    for i in range(0,len(arr)):
        if arr[i]==x:
            return i
    return 0

arr=[ 1,5,7,9,4,6,3]
print(ls(arr,9))