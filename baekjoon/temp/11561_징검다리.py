n = int(input())
answer = []

for i in range(n) :
	num = int(input())
	start = 1
	end = num
	temp = -1
	while True:
		if start > end :
			break
		mid = (start+end)//2
		if mid % 2 == 0 :
			sum_ = (1 + mid) * (mid//2)
		else :
			sum_ = ((1 + mid) * (mid//2)) + ((1 + mid)//2)

		if sum_ > num :
			end = mid - 1
		elif sum_ == num :
			temp = mid
			break
		else :
			temp = mid
			start = mid + 1

	answer.append(temp)

for i in range(len(answer)) :
	print(answer[i])