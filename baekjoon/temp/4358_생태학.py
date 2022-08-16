import sys

tree_count = {}
all_count = 0
while True :
	name = sys.stdin.readline().strip()
	if name == '' :
		break
	else :
		if name not in tree_count :
			tree_count[name] = 1
		else :
			tree_count[name] += 1
		all_count += 1

dic_sort =dict(sorted(tree_count.items()))

for i in dic_sort:
	print('%s %0.4f'%(i,(dic_sort[i] * 100 / all_count)))