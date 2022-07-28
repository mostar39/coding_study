from collections import deque

n, m, k, x = map(int,input().split())
array = [[] for i in range(n+1)]

for i in range(m) :
	start, end = map(int,input().split())
	array[start].append(end)

count = [0 for i in range(n+1)]

q = deque()

for i in array[x] :
	q.append([x,i])
	count[i] += 1

while q :
	s, f = q.popleft()
	for i in array[f] :
		if count[i] == 0 :
			count[i] = count[f] + 1
			q.append([f,i])
		# count[i] = min(count[f]+1,count[i])

check = 0
for i in range(len(count)) :
	if count[i] == k :
		check = 1
		print(i)

if check == 0 :
	print(-1)




