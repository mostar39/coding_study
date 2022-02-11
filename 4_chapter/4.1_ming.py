import time

number = int(input())
path = list(map(str, input().split()))

row = 1
col = 1
start = time.time()
for i in range(len(path)) :
	if (path[i] == 'L')&(col!=1) :
		col = col - 1
	elif (path[i] == 'R')&(col!=number) :
		col = col + 1
	elif (path[i] == 'U')&(row!=1) :
		row = row - 1
	elif (path[i] == 'D')&(row!=number) :
		row = row + 1

end = time.time()
print(end)
print(start)
print(str(row)+' '+str(col))