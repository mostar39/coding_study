import sys

n = int(sys.stdin.readline())
int(sys.stdin.readline())

list_ = list(map(int, sys.stdin.readline().split()))

q = []
count = []

for i in range(len(list_)) :
	if list_[i] in q :
		index_ = q.index(list_[i])
		count[index_] += 1
	else :
		if len(q) < n :
			q.append(list_[i])
			count.append(1)
		else:
			small = min(count)
			for j in range(len(count)) :
				if small == count[j] :
					temp=j
					break
			del q[temp]
			del count[temp]
			q.append(list_[i])
			count.append(1)
q.sort()
for i in range(len(q)) :
	print(q[i], end= ' ')