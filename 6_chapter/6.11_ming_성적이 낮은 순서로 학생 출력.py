n = int(input())

array = []
for i in range(n) :
	input_data = input().split()
	array.append((input_data[0],int(input_data[1])))

def setting(data) :
	return data[1]

new_array = sorted(array,key=setting)

for i in range(n) :
	print(new_array[i][0], end=' ')