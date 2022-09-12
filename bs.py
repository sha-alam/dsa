def bs(arr,x):
    n=len(arr)
    low=0
    high=n-1
    while low<=high:
        mid=low+high//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            high=mid-1
        else:
            low=mid+1
    return -1

arr=[1,3,5,6,8,9]
print(bs(arr,10))