import sys

n,m = map(int,sys.stdin.readline().split())
divide_num = int(sys.stdin.readline().strip())
row= [0, m]
col = [0, n]

for i in range(divide_num) :
	temp = list(map(int,sys.stdin.readline().split()))
	if temp[0]==0 :
		row.append(temp[1])
	else :
		col.append(temp[1])

row.sort()
col.sort()

x_list = [row[i+1]-row[i] for i in range(len(row)-1)]
y_list = [col[i+1]-col[i] for i in range(len(col)-1)]

print(max(x_list)*max(y_list))

