def bbs(arr):
    n=len(arr)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
arr=[1,5,4,6,3,2,8,5,6,4,7,1,5,7,5]
bbs(arr)
print(arr)