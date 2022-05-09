import sys

n = int(sys.stdin.readline())
num_list = list(map(int,sys.stdin.readline().split()))
num_list.sort()
sum_ = sum(num_list)

answer = 0
for i in range(len(num_list)-1) :
	sum_ -= num_list[i]
	answer += num_list[i] * sum_

print(answer)