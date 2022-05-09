import sys

max_, _ = map(int,sys.stdin.readline().split())
array = list(map(int,sys.stdin.readline().split()))

array.sort(reverse=True)

check = 0
answer = ''
for i in range(len(str(max_))) :
	if check == 1 :
		temp_=[str(max(array))] * (len(str(max_))-i)
		ans = ''.join(temp_)
		answer += ans
		break
	for j in range(len(array)) :
		if int(str(max_)[i]) > array[j] :
			answer += str(array[j])
			check = 1
			break
		elif int(str(max_)[i]) == array[j] :
			answer += str(array[j])
			break
		if j==len(array)-1 :
			check = 1

print(answer)
