def merge_sort(arr):
    size = len(arr)
    if size > 1:
        mid = size // 2
        l_a = arr[:mid]
        r_a = arr[mid:]
        merge_sort(l_a)
        merge_sort(r_a)
        size_la = len(l_a)
        size_ra = len(r_a)
        p = 0
        q = 0
        r = 0
        while p < size_la and q < size_ra:
            if l_a[p] >= r_a[q]:
                arr[r] = r_a[q]
                q += 1
            else:
                arr[r] = l_a[p]
                p += 1
            r += 1
        while p < size_la:
            arr[r] = l_a[p]
            p += 1
            r += 1
        while q < size_ra:
            arr[r] = r_a[q]
            q += 1
            r += 1


array = list(map(int, input("Enter your Array : ").split()))
print("Your Array is :", array)
merge_sort(array)
print("Sorted Array:\n")
print(array)
