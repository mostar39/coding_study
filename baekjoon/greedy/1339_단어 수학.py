from functools import reduce

num = int(input())
str_list = []
max_len = 0

for i in range(num) :
	str_list.append(list(map(str, input())))
	max_len = max(max_len, len(str_list[i]))


word = list(set(reduce(lambda x, y : x + y,str_list)))
str_list.sort(key= lambda x:len(x), reverse=True)

visited = [0]*len(word)


for i in range(len(str_list)) :
	for j in range(len(str_list[i])) :
		try:
			if i == 0:
				temp = str(9 - j)
				visited[word.index(str_list[i][j])] = temp
			elif word[word.index(str_list[i][j])] !=0 :
				temp = str(9 - (i * len(str_list[i - 1]) - j))
				visited[word.index(str_list[i][j])] = temp
		except :
			pass



