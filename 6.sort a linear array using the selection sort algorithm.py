def selection_sort(arr, size):
	for i in range(size):
		mn = i
		for j in range(i + 1, size):
			if arr[j] < arr[mn]:
				mn = j
		arr[i], arr[mn] = arr[mn], arr[i]


array = list(map(int, input("Enter an arr: ").split()))
selection_sort(array, len(array))
print('After selection sort: ', array)
