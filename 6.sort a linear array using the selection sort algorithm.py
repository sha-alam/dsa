def selection_sort(arr, size):
	for idx in range(size):
		min_i = idx
		for j in range(idx + 1, size):
			if arr[j] < arr[min_i]:
				min_i = j
		arr[idx], arr[min_i] = arr[min_i], arr[idx]


array = list(map(int, input("Enter an arr: ").split()))
selection_sort(array, len(array))
print('After selection sort: ', array)
