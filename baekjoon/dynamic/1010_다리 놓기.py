import sys
case = int(sys.stdin.readline())

#: nCm
def factorial(k) :
	fact = 1
	for i in range(1,k+1) :
		fact *= i
	return fact

def combination(n,r) :
	return factorial(n)/(factorial(n-r) * factorial(r))


for i in range(case) :
	n,m = map(int,sys.stdin.readline().split())
	d = [0] * (m+1)


	for j in range(n,m+1) :
		d[j] = d[j-1] + combination(j-1,n-1)

	print(int(d[m]))
