n = int(input())
count = 0

for i in range(n) :
	sign = 0
	str_ = input()
	unseen = []
	last_text = '-1'

	for j in range(len(str_)) :
		if str_[j] not in unseen :
			unseen.append(str_[j])
			last_text = str_[j]
		else :
			if last_text != str_[j] :
				sign = 1
				break

	if sign== 0 :
		count += 1

print(count)
