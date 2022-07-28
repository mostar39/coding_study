import heapq

n = int(input())
array = [list(map(int,input().split())) for i in range(n)]
array.sort(key=lambda x:x[1])

temp = []

for pay, day in array :
	heapq.heappush(temp,pay)
	if len(temp) > day :
		heapq.heappop(temp)
print(sum(temp))