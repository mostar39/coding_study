from collections import deque

n, m = map(int,input().split())
array = []

for i in range(1,n+1) :
	how_many = int(input())
	if i%2 == 1 :
		temp = [1]*how_many + [0]*(m-how_many)
		array.append(temp)
	else :
		temp = [0] * (m - how_many) + [1] * how_many
		array.append(temp)

col_array = deque(list(zip(*array)))
del array

min_ = n
count = 0
while col_array :
	col = col_array.pop()
	sum_ = sum(list(col))
	if sum_ < min_ :
		count = 1
		min_ = sum_
	elif sum_ == min_ :
		count += 1
	else :
		continue

print(min_, count)

# =============================================================================

n, m = map(int,input().split())
array = [0]*m

for i in range(1,n+1) :
	how_many = int(input())
	if i%2 == 1 :
		for j in range(how_many) :
			array[j] += 1
	else :
		for j in range(m-1,m-how_many-1,-1) :
			array[j] += 1

array.sort()
min_ = array[0]

start = 0
end = len(array)-1
check = -1

while True :
	if start > end :
		break
	mid = (start+end)//2
	if array[mid] != min_ :
		end = mid-1
	else :
		check = mid
		start = mid+1


print(min_, mid+1)

#==================================

n, m = map(int,input().split())
up = [0]*(m+1)
down = [0] *(m+1)

min_ = n
count = 0

for i in range(n) :
	if i % 2 == 0 :
		down[int(input())] += 1
	else :
		up[int(input())] += 1

for i in range(m-1,0,-1) :
	down[i] += down[i+1]
	up[i] += up[i+1]

for i in range(1,m+1) :
	if min_ > (down[i]+up[m-i+1]) :
		min_ = down[i]+up[m-i+1]
		count = 1
	elif min_ == (down[i]+up[m-i+1]) :
		count += 1

print(min_,count)