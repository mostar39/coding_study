from collections import deque
n = int(input())

choice_array = list(map(int,input().split()))
answer = deque(range(1,n+1))
first = deque()

for i in range(len(answer)) :
	what = answer.popleft()
	method = choice_array.pop()

	if method == 1 :
		first.appendleft(what)
	elif method == 2 :
		first.insert(1,what)
	elif method == 3 :
		first.append(what)

print(*first)
