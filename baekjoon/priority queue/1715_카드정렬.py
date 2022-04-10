import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n) :
	temp = int(sys.stdin.readline())
	heapq.heappush(heap,temp)

sum_ = 0
while len(heap)>=2 :
	a=heapq.heappop(heap)
	b=heapq.heappop(heap)
	heapq.heappush(heap,a+b)
	sum_ += a+b

print(sum_)
