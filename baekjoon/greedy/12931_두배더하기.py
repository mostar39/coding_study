import sys

n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))

count = 0
while True :
	zero = 0
	for i in range(len(array)) :
		if array[i] % 2 == 1 :
			array[i] = array[i] - 1
			count += 1
		if array[i] == 0 :
			zero += 1

	if zero == n :
		break

	else :
		for i in range(len(array)) :
			array[i] /= 2

		count += 1

print(count)