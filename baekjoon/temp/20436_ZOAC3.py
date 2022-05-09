import sys

dict_ = {'q':[0,0,0], 'w':[0,1,0], 'e':[0,2,0], 'r':[0,3,0], 't':[0,4,0], 'y':[0,5,1],
		 'u':[0,6,1], 'i':[0,7,1], 'o':[0,8,1], 'p':[0,9,1], 'a':[1,0,0], 's':[1,1,0],
		 'd':[1,2,0], 'f':[1,3,0], 'g':[1,4,0], 'h':[1,5,1], 'j':[1,6,1], 'k':[1,7,1],
		 'l':[1,8,1], 'z':[2,0,0], 'x':[2,1,0], 'c':[2,2,0], 'v':[2,3,0], 'b':[2,4,1],
		 'n':[2,5,1], 'm':[2,6,1]}

start , end = sys.stdin.readline().split()
left_hand = dict_[start][0:2]
right_hand = dict_[end][0:2]

word = list(map(str,sys.stdin.readline().strip()))

time = 0
for i in range(len(word)) :
	where = dict_[word[i]]
	if where[2] == 0 :
		left = abs(left_hand[0]-where[0]) + abs(left_hand[1]-where[1])
		time += (left+1)
		left_hand = where[0:2]
	else:
		right = abs(right_hand[0]-where[0]) + abs(right_hand[1]-where[1])
		time += (right+1)
		right_hand = where[0:2]


print(time)