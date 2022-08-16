str_ = input()

answer = ''
temp = ''
sign = 0

for i in range(len(str_)) :
	if str_[i] == '<' :
		sign = 1
		if len(temp) != 0 :
			new_temp = ''
			for j in range(len(temp)) :
				new_temp += temp[len(temp)-1-j]
			temp = ''
			answer += new_temp
	elif str_[i] == '>' :
		sign = 2
		temp += str_[i]
		answer += temp
		temp = ''
		continue
	elif sign == 2 and str_[i] == ' ' :
		new_temp = ''
		for j in range(len(temp)) :
			new_temp += temp[len(temp) - 1 - j]
		temp = ''
		answer += (new_temp + ' ')
		continue
	elif i == 0 :
		sign = 2
	elif i == len(str_)-1 :
		temp += str_[i]
		new_temp = ''
		for j in range(len(temp)):
			new_temp += temp[len(temp) - 1 - j]
		temp = ''
		answer += (new_temp)
		continue
	temp += str_[i]

print(answer)