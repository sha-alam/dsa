def mergeSort(arr):
    size=len(arr)
    if size>1:
        mid=size//2
        la=arr[:mid]
        ra=arr[mid:]
        mergeSort(la)
        mergeSort(ra)
        las=len(la)
        ras=len(ra)
        p=0
        q=0
        r=0
        while p<las and q<ras:
            if la[p]<ra[q]:
                arr[r]=la[p]
                p+=1
            else:
                arr[r]=ra[q]
                q+=1
            r+=1
        while p<las:
            arr[r]=la[p]
            p+=1
            r+=1
        while q<ras:
            arr[r]=ra[q]
            q+=1
            r+=1

array=list(map(int,input().split()))
mergeSort(array)
print(array)