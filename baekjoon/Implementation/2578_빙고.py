import sys

my_bingo = [list(map(int,sys.stdin.readline().split())) for i in range(5)]
answer = []
for i in range(5) :
	answer = answer + list(map(int,sys.stdin.readline().split()))

index = 0


while bingo<3:
	bingo = 0
	for i in range(5) :
		for j in range(5) :
			if my_bingo[i][j] == answer[index] :
				my_bingo[i][j] = 0
	cross_1 = 0
	cross_2 = 0

	for i in range(5) :
		if sum(my_bingo[i])== 0 :
			bingo += 1
		if sum(list(list(zip(*my_bingo))[i])) == 0 :
			bingo += 1
		cross_1 = cross_1+my_bingo[i][i]
		cross_2 = cross_2+my_bingo[i][4-i]
		if i==4 and cross_1==0 :
			bingo += 1
		if i==4 and cross_2==0 :
			bingo += 1
	index += 1

print(index)
