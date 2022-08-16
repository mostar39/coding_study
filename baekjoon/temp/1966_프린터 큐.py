from collections import deque

test = int(input())
answer = []
for i in range(test) :
	n, m = map(int,input().split())
	list_ = list(enumerate(map(int,input().split())))
	sorted_ = sorted(list(list(zip(*list_))[1]), reverse=True)
	q = deque(list_)
	k = 0
	count = 0
	while q :
		target = sorted_[k]
		hey = q.popleft()
		if hey[1] != target :
			q.append(hey)
		else :
			count += 1
			k += 1
			if hey[0] == m :
				break
	answer.append(count)

for i in answer :
	print(i)