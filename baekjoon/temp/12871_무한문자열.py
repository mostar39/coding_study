import sys
import math

str_1 = sys.stdin.readline().strip()
str_2 = sys.stdin.readline().strip()

num = math.lcm(len(str_1),len(str_2))

str_1_num = num//len(str_1)
str_2_num = num//len(str_2)

if str_1 * (str_1_num) == str_2 * (str_2_num) :
	print(1)
else :
	print(0)