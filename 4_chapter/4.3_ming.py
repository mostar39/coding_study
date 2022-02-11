place = input()

str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

col = int(str.index(place[0])) + 1
row = int(place[1])

count = 0

problem = [
	[2,1],
	[2,-1],
	[-2,1],
	[-2,-1],
	[1,2],
	[1,-2],
	[-1,2],
	[-1,-2]
]

for i in range(len(problem)) :
	temp_x = row
	temp_y = col

	temp_x = temp_x + problem[i][0]
	temp_y = temp_y + problem[i][1]

	if (temp_x>=1) & (temp_y>=1) & (temp_x<=8) & (temp_y<=8):
		count= count+1

print(count)



