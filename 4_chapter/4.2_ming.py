import time

number = int(input())
number = number * 3600 + 3599

hour = number // 3600
min = (number % 3600) // 60
second = (number % 3600) % 60

count = 0

start = time.time()

for i in range(number) :
	hour = (i+1) // 3600
	min = ((i+1) % 3600) // 60
	second = ((i+1) % 3600) % 60

	if ('3' in str(hour)) or ('3' in str(min)) or ('3' in str(second)) :
		count = count + 1


end = time.time()

print(end-start)
print(count)
