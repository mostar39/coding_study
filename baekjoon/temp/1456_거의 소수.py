a, b = map(int,input().split())

array = [False] * (int(b**0.5)+1)

for i in range(2, (int(b**0.5)+1)) :
	sign = 0
	for j in range(2, (int(i**0.5)+1)) :
		if i%j == 0 :
			sign = 1
			break
	if sign == 0 :
		array[i] = True

cnt = 0
for i in range(len(array)) :
	if array[i] :
		num = i * i
		while True :
			if num > b :
				break
			if (a <= num <= b) :
				cnt += 1
			num = num * i
print(cnt)

# =========================================

a, b = map(int,input().split())


cnt = 0

for i in range(2, (int(b**0.5)+1)) :
	sign = 0
	for j in range(2, (int(i**0.5)+1)) :
		if i%j == 0 :
			sign = 1
			break
	if sign == 0 :
		num = i * i
		while True :
			if num > b :
				break
			if (a <= num <= b) :
				cnt += 1
			num = num * i

print(cnt)