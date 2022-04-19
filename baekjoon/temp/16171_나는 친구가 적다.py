import sys

str_ = str(sys.stdin.readline().strip())
answer = str(sys.stdin.readline().strip())
new_str = ''
for i in range(len(str_)) :
	if str_[i].isdigit() == False :
		new_str += str_[i]

if answer in new_str :
	print(1)
else :
	print(0)