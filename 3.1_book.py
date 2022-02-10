import time

money = int(input())
count = 0

coin_types = [500,100,50,10]

start = time.time()

for coin in coin_types :
	count += money //coin
	money %= coin

end = time.time()

print('=============time==============')
print(end)
print(start)
print(end-start)
print('===============================')

print(count)