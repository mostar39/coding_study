from collections import deque

n, k = map(int,input().split())
array = list(map(int,input().split()))

q = deque()
q.append([0]+list(range(1,n)))
sign = 0

hi = [0] * n
hi[0] = 1

while q :
	if sign == 1 :
		break
	temp = q.popleft()
	start = temp[0]
	go_list = temp[1:]

	for i in go_list :
		if ((i-start) * (1 + abs(array[start]-array[i])) <= k) and hi[i] == 0 :
			hi[i]=1
			real_temp = [i] + list(range(i + 1, n))
			if i == n-1 :
				sign = 1
				break
			else :
				q.append(real_temp)

if sign == 1 :
	print('YES')
else :
	print('NO')
