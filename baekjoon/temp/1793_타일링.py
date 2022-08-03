d = [0] * 251

d[0] = 1
d[1] = 1
d[2] = 3

for i in range(3,len(d)) :
	d[i] = d[i-1] + 2*d[i-2]

while True :
	try :
		print(d[int(input())])
	except :
		break