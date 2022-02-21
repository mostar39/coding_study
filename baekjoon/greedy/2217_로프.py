n = int(input())
weight = [int(input()) for _ in range(n)]

weight.sort(reverse=True)

max_list = []
for i in range(n) :
	max_list.append(weight[i] * (i+1))

print(max(max_list))