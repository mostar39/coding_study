import sys

n = sys.stdin.readline().strip()
array = list(map(int, sys.stdin.readline().split()))
array.sort()
m = sys.stdin.readline().strip()
customer = list(map(int, sys.stdin. readline().split()))

def binary(array, target,start, end) :
	if start>end :
		return None
	mid = (start + end) // 2
	if array[mid] == target :
		return mid
	elif array[mid] > target :
		return binary(array, target, start, mid-1)
	elif array[mid] < target :
		return binary(array, target, mid+1, end)

for i in range(len(customer)) :
	answer = binary(array, customer[i], 0, len(array)-1)
	if answer==None :
		print('No', end=' ')
	else :
		print('Yes', end = ' ')