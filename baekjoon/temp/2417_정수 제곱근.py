n = int(input())

start = 0
end = 2**32

answer = -1

while True :
	if start > end :
		break
	mid = (start+end)//2
	if mid**2<n :
		start = mid + 1
	elif mid**2 > n :
		answer = mid
		end = mid - 1
	else :
		answer = mid
		break


print(answer)