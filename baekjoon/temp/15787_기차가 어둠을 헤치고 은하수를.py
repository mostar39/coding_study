n, m = map(int,input().split())
array = [[0] * 21 for _ in range(n)]

def one(train, num) :
	if train[num] == 1 :
		return train
	else :
		train[num] = 1
		return train

def two(train, num) :
	if train[num] == 0 :
		return train
	else :
		train[num] = 0
		return train

def three(train) :
	new_train = [0] * 21
	for i in range(1,len(train)) :
		if train[i] == 1 and i != 20 :
			new_train[i+1] = train[i]

	return new_train

def four(train) :
	new_train = [0] * 21
	for i in range(1,len(train)) :
		if train[i] == 1 and i != 1:
			new_train[i-1] = train[i]
	return new_train

for i in range(m) :
	# hey, tr, sit
	hey = list(map(int,input().split()))
	ne_tr = list(array[hey[1]-1])
	if hey[0] == 1 :
		new = one(ne_tr,hey[2])
	elif hey[0] == 2:
		new = two(ne_tr,hey[2])
	elif hey[0] == 3 :
		new = three(ne_tr)
	else :
		new= four(ne_tr)
	array[hey[1]-1] = new


check = []
for i in range(n) :
	if array[i] not in check :
		check.append(array[i])

print(len(check))