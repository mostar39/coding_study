N, M = map(int,input().split())
min_list = []
for i in range(N) :
	list_temp = list(map(int,input().split()))
	list_temp.sort()
	min_list.append(list_temp[0])


min_list.sort()
print(min_list[N-1])
