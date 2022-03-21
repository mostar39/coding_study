array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
new_array = []

#===============================================

for i in range(len(array)) :
	min_num = min(array)
	min_index = array.index(min_num)
	new_array.append(array[min_index])
	array[min_index]=99999999

print(new_array)

#===============================================
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)) :
	min_index = i
	for j in range(i+1, len(array)) :
		if array[min_index] > array[j] :
			min_index = j
	array[i], array[min_index] = array[min_index],array[i]

print(array)