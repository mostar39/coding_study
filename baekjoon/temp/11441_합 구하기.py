n = int(input())
first = list(map(int,input().split()))
array = [0] * (n+1)
for i in range(1,n+1) :
	array[i] = array[i-1] + first[i-1]

times = int(input())
answer = []
for j in range(times) :
	start, end = map(int,input().split())
	answer.append(array[end]-array[start-1])

for i in answer :
	print(i)