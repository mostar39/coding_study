n = int(input())
gram = list(map(int,input().split()))
m = int(input())
circle = list(map(int,input().split()))

dp = [[0] * 15001 for _ in range(n+1)]
possible = []

def calculation(left, right, num) :
	new = abs(left-right)

	if new not in possible:
		possible.append(new)

	if num == n :
		return 0

	if dp[num][new] == 0 :
		calculation(left+gram[num], right, num+1)
		calculation(left, right+gram[num], num+1)
		calculation(left, right, num+1)

		dp[num][new] = 1

calculation(0,0,0)
for i in range(len(circle)) :
	if circle[i] in possible :
		print('Y', end= ' ')
	else :
		print('N', end = ' ')
