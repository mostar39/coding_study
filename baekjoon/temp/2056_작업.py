n = int(input())
time = [0] * (n+1)

array = {}

for i in range(1,n+1) :
	temp = list(map(int,input().split()))
	time[i] = temp[0]
	after = temp[2:]
	array[i] = []
	for j in range(len(after)) :
		array[i].append(after[j])

for i in range(1, n+1) :
	if len(array[i]) != 0 :
		temp_time = 0
		for j in array[i] :
			temp_time = max(temp_time, time[j])
		time[i] += temp_time

print(max(time))

