import time

n, m = map(int,input().split())

start = time.time()

result = 0
for i in range(n) :
	data = list(map(int,input().split()))
	min_value = min(data)
	result = max(result, min_value)

end = time.time()
print(end - start)
print(result)