n, m, time = map(int,input().split())

array = [list(map(int,input().split())) for i in range(n)]


def shake_it(num, arr) :
	if num == 1 :
		arr=arr[::-1]
		return arr
	elif num == 2 :
		arr = list(zip(*arr))
		arr = arr[::-1]
		arr = list(zip(*arr))
		return arr
	elif num == 3 :
		arr = arr[::-1]
		arr = list(zip(*arr))
		return arr
	elif num == 4 :
		arr = list(zip(*arr))
		arr = arr[::-1]
		return  arr
	elif num == 5 :
		temp = [[0]*len(arr[0]) for _ in range(len(arr))]
		for k in range(len(arr)) :
			for t in [0,1] :
				if k < len(arr)//2 and t == 0 :
					temp[k][len(arr[0])//2:] = arr[k][:len(arr[0])//2]
				elif k < len(arr)//2 and t == 1 :
					temp[k+len(arr)//2][len(arr[0])//2:] = arr[k][len(arr[0])//2:]
				elif k >= len(arr)//2 and t == 0 :
					temp[k-len(arr)//2][:len(arr[0])//2] = arr[k][:len(arr[0])//2]
				else :
					temp[k][:len(arr[0])//2] = arr[k][len(arr[0])//2:]
		return temp
	elif num == 6 :
		temp = [[0] * len(arr[0]) for _ in range(len(arr))]
		for k in range(len(arr)) :
			for t in [0,1] :
				if k < len(arr)//2 and t == 0 :
					temp[k+len(arr)//2][:len(arr[0])//2] = arr[k][:len(arr[0])//2]
				elif k < len(arr)//2 and t == 1 :
					temp[k][:len(arr[0])//2] = arr[k][len(arr[0])//2:]
				elif k >= len(arr)//2 and t == 0 :
					temp[k][len(arr[0])//2:] = arr[k][:len(arr[0])//2]
				else:
					temp[k-len(arr)//2][len(arr[0])//2:] = array[k][len(arr[0])//2:]
		return temp

what = list(map(int,input().split()))
for i in range(len(what)) :
	array = shake_it(what[i],array)

for i in range(len(array)) :
	print(*array[i])