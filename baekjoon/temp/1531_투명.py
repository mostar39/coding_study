import sys

n,m = map(int,sys.stdin.readline().split())
array = [[0]*100 for i in range(100)]
count = 0
for i in range(n) :
	x_min, y_min, x_max, y_max = map(int,sys.stdin.readline().split())
	for p in range(x_min-1, x_max) :
		for q in range(y_min-1,y_max) :
			if array[p][q] == -1 :
				continue
			else:
				array[p][q] += 1
				if array[p][q] > m :
					count += 1
					array[p][q] = -1

print(count)
