array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort_ming(array_list) :
	if len(array_list) <= 1 :
		return array_list
	else :
		pivot = array_list[0]
		tail = array_list[1:]

		left = [i for i in tail if i<=pivot]
		right = [x for x in tail if x > pivot]

		return quick_sort_ming(left) + [pivot] + quick_sort_ming(right)



print(quick_sort_ming(array))