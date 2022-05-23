n = int(input())
a_list = list(map(int,input().split()))
a_list.sort()

m = int(input())
b_list = list(map(int,input().split()))

def binary(target) :
	left = 0
	right = len(a_list)-1
	while True :
		mid = (left + right) // 2
		if left > right :
			return False
		if a_list[mid] < target :
			left = mid+1
		elif a_list[mid] > target :
			right = mid-1
		elif a_list[mid] == target :
			return True

for i in range(len(b_list)) :
	if binary(b_list[i]) :
		print(1)
	else :
		print(0)
