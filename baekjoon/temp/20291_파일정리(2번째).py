n = int(input())

dict_ = {}
list_ = []

for i in range(n) :
	hey = list(input().split('.'))[1]
	if hey not in dict_ :
		dict_[hey] = 1
		list_.append(hey)
	else :
		dict_[hey] += 1

list_.sort()

for i in range(len(list_)) :
	print(list_[i], dict_[list_[i]])