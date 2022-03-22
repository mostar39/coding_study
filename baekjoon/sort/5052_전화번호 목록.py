import sys
test = int(input())
def check (array) :
	for i in range(len(array)-1) :
		if array[i] == array[i+1][0:len(array[i])]:
			print("NO")
			return
	print("YES")

for i in range(test) :
	n = int(input())
	array = [sys.stdin.readline().strip() for i in range(n)]
	array.sort()
	check(array)

