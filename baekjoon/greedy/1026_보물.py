n = int(input())

all_thing = []

for i in range(2) :
	temp = list(map(int, input().split()))
	all_thing.append(temp)

mul = 0
all_thing[0].sort()
for i in range(n) :
	max_num=max(all_thing[1])
	max_num_index = all_thing[1].index(max_num)
	mul = mul+ all_thing[0][i]*max(all_thing[1])
	all_thing[1][max_num_index] = -1

print(mul)
