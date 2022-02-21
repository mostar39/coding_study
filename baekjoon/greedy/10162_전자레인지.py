t = int(input())
time = [300,60,10]


for i in range(3) :
	if (t<=0) & i ==2 :
		break
	elif t%10 != 0:
		print_num = -1
		print(print_num)
		break
	else :
		print_num = (t//time[i])
		print(print_num, end=' ')
		t -= (t // time[i]) * time[i]

