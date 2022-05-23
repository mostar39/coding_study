from collections import deque

n = int(input())
flower = [(list(map(int, input().split()))) for i in range(n)]
flower.sort(key= lambda x:(x[0],x[1],x[2],x[3]))

q = deque()

for i in range(n) :
	start_m, start_d, end_m, end_d=flower[i]
	if start_m < 3 :
		q.append([i,start_m, start_d, end_m, end_d, 1])
	elif (start_m == 3) and (start_d == 1) :
		q.append([i,start_m, start_d, end_m, end_d, 1])
	else :
		break

min_= 9999999

while q :
	index, start_m, start_d, end_m, end_d, count= q.popleft()

	if end_m > 11 :
		min_ = min(min_,count)
		continue

	start = index+1
	end = n-1

	check = -1

	while True :
		if start > end :
			break
		mid = (start+end)//2
		if list(zip(*flower))[0][mid]<end_m :
			check = mid
			start = mid+1
		elif (list(zip(*flower))[0][mid] == end_m) and (list(zip(*flower))[1][mid]<=end_d) :
			check = mid
			start = mid+1
		else :
			end = mid-1

	if check != -1 :
		q.append([check]+flower[check]+[count+1])

print(min_)

#====================================================================================================


n = int(input())
flower = [(list(map(int, input().split()))) for i in range(n)]
flower.sort(key= lambda x:(x[0],x[1],x[2],x[3]))

start = 0
end = n - 1

count = 0
while True :
	if count == 0 :
		index_ = -1
		for i in range(len(flower)) :
			if flower[i][0] < 3 :
				index_ = i
			elif (flower[i][0] == 3) and (flower[i][1] == 1) :
				index_ = i
			else :
				break
		count += 1

	start = index_ + 1
	end = n - 1

	check = []


	while True:
		if start > end:
			break
		mid = (start + end) // 2
		if list(zip(*flower))[0][mid] < flower[index_][2]:
			check.append(mid)
			start = mid + 1
		elif (list(zip(*flower))[0][mid] == flower[index_][2]) and (list(zip(*flower))[1][mid] <= flower[index_][3]):
			check.append(mid)
			start = mid + 1
		else:
			end = mid - 1

	if len(check) == 0 :
		break
	else :
		count+=1
		index_=max(check)

	if flower[index_][2] > 11 :
		break

print(count)






