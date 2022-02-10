import time

money = int(input())
category = [500,100,50,10]

coin = 0

start = time.time()

for i in range(len(category)) :
	coin_temp = money//category[i]
	print(coin_temp)
	coin += coin_temp
	money -= coin_temp*category[i]

end = time.time()

print('==============ming=================')
print(end)
print(start)
print('ming_성능 : ', end - start)
print('==============coin=================')
print(coin)

## 시간이 예제에서 하는 것보다 오래걸림 ㅜ_ㅜ