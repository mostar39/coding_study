import heapq
import sys

n = int(sys.stdin.readline())

heap = []

for i in range(n):
	temp = list(map(int, sys.stdin.readline().split()))
	if not heap:
		for j in temp:
			heapq.heappush(heap, j)
	else:
		for j in temp:
			if j > heap[0]:
				heapq.heappush(heap, j)
				heapq.heappop(heap)
print(heap[0])
