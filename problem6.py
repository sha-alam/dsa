# Author: MD.Shahdat Hossain Bhuian
def selectionSort(arr, size):	
	for idx in range(size):
		min_index = idx
		for j in range(idx + 1, size):
			if arr[j] < arr[min_index]:
				min_index = j
		arr[idx], arr[min_index] = arr[min_index], arr[idx]

arr = list(map(int,input("Enter an arr: ").split()))
selectionSort(arr, len(arr))
print('After selection sort: ',arr)
