n = int(input())

array= [[0]*100 for i in range(100)]
cnt = 0

for i in range(n) :
	x, y = map(int,input().split())
	for p in range(10) :
		for q in range(10) :
			if array[x+p][y+q] == 0 :
				cnt += 1
				array[x+p][y+q] = 1

print(cnt)