import sys

while 1:
	try:
		start, end = map(int, sys.stdin.readline().split())
		count = 0
		for i in range(start, end+1) :
			if len(str(i))==len(list(set(map(int,str(i))))) :
				count+=1
		print(count)
	except:
		break

