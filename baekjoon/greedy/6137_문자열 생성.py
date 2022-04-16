import sys

str_dict = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10,
			'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20,
			'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}

n = int(sys.stdin.readline())
list_ = [sys.stdin.readline().strip() for i in range(n)]

left, right = 0, len(list_)-1
answer = ''

while True :
	if left>right :
		break
	if left == right :
		answer += list_[left]
		break
	if str_dict[list_[left]] < str_dict[list_[right]] :
		answer += list_[left]
		left += 1
	elif str_dict[list_[left]] > str_dict[list_[right]] :
		answer += list_[right]
		right -= 1
	elif str_dict[list_[left]] == str_dict[list_[right]] :
		if str_dict[list_[left+1]] < str_dict[list_[right-1]] :
			answer += list_[left]
			left += 1
		elif str_dict[list_[left+1]] > str_dict[list_[right-1]] :
			answer += list_[right]
			right -= 1
		else :
			answer += list_[left]
			left += 1

print(answer)

