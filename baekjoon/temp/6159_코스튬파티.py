n,s = map(int,input().split())
cow_list = [int(input()) for i in range(n)]

cow_list.sort(reverse=True)

def binary(cow_list, index_) :
	target = cow_list[index_]
	cow_list_new = list(cow_list)[index_+1:]
	start = 0
	end = len(cow_list_new) - 1
	hello = -1
	while True :
		if start>end :
			break
		mid = (start + end) // 2
		if target + cow_list_new[mid] == s :
			hello = mid
			break
		elif target + cow_list_new[mid] < s :
			hello = mid
			end = mid - 1
		elif target + cow_list_new[mid] > s :
			start = mid + 1
	if hello == -1 :
		ok = 0
	else :
		ok = len(cow_list_new) - hello
	return ok

all = 0
for i in range(len(cow_list)-1) :
	all += binary(cow_list,i)

print(all)