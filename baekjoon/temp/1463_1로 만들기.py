dp = [0] * 1000001
n = int(input())

dp[2] = 1
dp[3] = 1

for i in range(4,len(dp)) :
	temp = []
	if i % 3 == 0 :
		temp.append(dp[i//3] + 1)
	if i % 2 == 0 :
		temp.append(dp[i//2] + 1)
	temp.append(dp[i-1] + 1)
	dp[i] = min(temp)

print(dp[n])