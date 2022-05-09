import sys


king, rock, num = sys.stdin.readline().split()

real_king = [int(king[1])-1,ord(king[0])-65]
real_rock = [int(rock[1])-1,ord(rock[0])-65]

moving = [sys.stdin.readline().strip() for i in range(int(num))]
dic_moving = {'R':[0,1],'L':[0,-1],'B':[-1,0],'T':[1,0], 'RT':[1,1], 'LT':[1,-1], 'RB':[-1,1], 'LB':[-1,-1]}

for i in range(int(num)) :
	king_temp_x = real_king[0]+dic_moving[moving[i]][0]
	king_temp_y = real_king[1]+dic_moving[moving[i]][1]
	rock_temp_x = real_rock[0]+dic_moving[moving[i]][0]
	rock_temp_y = real_rock[1]+dic_moving[moving[i]][1]
	if king_temp_x>=8 or king_temp_y>=8 or king_temp_x<=-1 or king_temp_y<=-1 :
		continue
	if [king_temp_x, king_temp_y] == real_rock :
		if rock_temp_x>=8 or rock_temp_y>=8 or rock_temp_x<=-1 or rock_temp_y<=-1 :
			continue
		else:
			real_king[0] = king_temp_x
			real_king[1] = king_temp_y
			real_rock[0] = rock_temp_x
			real_rock[1] = rock_temp_y
	else :
		real_king[0] = king_temp_x
		real_king[1] = king_temp_y

print(chr(real_king[1]+65)+str(real_king[0]+1))
print(chr(real_rock[1]+65)+str(real_rock[0]+1))

