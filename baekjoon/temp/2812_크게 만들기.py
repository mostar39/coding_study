n, k = map(int,input().split())
real_k = k
num = list(input())
answer = []

for i in range(n) :
	while answer and k>0 :
		if answer[-1] < num[i] :
			answer.pop()
			k -= 1
		else :
			break
	answer.append(num[i])

print(''.join(answer[:n-real_k]))