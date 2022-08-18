n = int(input())

array = [[' ']*(4*n-3) for i in range(4*n-3)]

hol = 1
jjack = 1
pair = 1

for i in range(0,len(array)) :
	if i == 0 :
		array[0] = ['*'] * (4 * n - 3)
	elif 1<=i<=(4*n-3)//2 :
		if i%2 == 1 :
			for k in range(0,hol*2,2) :
				array[i][k] = '*'
				array[i][-(k+1)] = '*'
			hol += 1
		elif i%2 == 0 :
			array[i] = ['*'] * (4 * n - 3)
			for k in range(1,jjack*2+1,2) :
				array[i][k]= ' '
				array[i][-(k+1)] = ' '
			jjack += 1
	else :
		array[i] = array[(4*n-3)//2-pair]
		pair+=1
	print(''.join(array[i]))

