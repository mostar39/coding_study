import time

h = int(input())

start = time.time()
count = 0
for i in range(h+1) :
	for j in range(60) :
		for k in range(60) :
			if '3' in str(i) + str(j) + str(k) :
				count += 1

end = time.time()
print(end-start)
print(count)