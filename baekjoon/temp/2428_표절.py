n = int(input())
array = list(map(float,input().split()))
array.sort(reverse = True)

answer = 0

for i in range(len(array)) :
	start = i+1
	end = n-1
	temp_answer = -1
	while True :
		if start > end :
			break
		mid = (start + end) // 2

		if array[i] * 0.9 <= array[mid] :
			temp_answer = mid
			start = mid+1
		elif array[i] * 0.9 > array[mid] :
			end = mid - 1


	if temp_answer != -1 :
		answer += (temp_answer-i)

print(answer)