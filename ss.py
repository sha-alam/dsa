def ss(arr):
    n=len(arr)
    for i in range(0,n):
        min=i
        for j in range(i+1,n):
            if arr[min]>arr[j]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]

arr=[2,5,3,4,6,2,1,7]
ss(arr)
print(arr)