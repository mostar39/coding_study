N, K = map(int, input().split())

number_1 = N%K
N = N - number_1
number_2 = 0
while (N!=1) :
	N = N/K
	number_2 = number_2+1

print(number_1+number_2)