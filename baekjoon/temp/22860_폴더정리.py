import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())

dict_ = {'main':{'0':[],'1':[]}}

for _ in range(n+m) :
	up, down, folder = map(str,input().strip().split())
	if up not in dict_:
		dict_[up] = {'0': [], '1': []}
	if folder == '1' :
		if down not in dict_:
			dict_[down] = {'0':[], '1':[]}
	dict_[up][folder].append(down)

test_case = int(input())

def search(folder_name) :
	global temp

	temp += dict_[folder_name]['0']
	sub_list = dict_[folder_name]['1']

	if sub_list == 0 :
		return

	for i in range(len(sub_list)) :
		search(sub_list[i])

answer = []
for _ in range(test_case) :
	str_list = input().strip().split('/')
	temp = []
	search(str_list[-1])
	set_temp = set(temp)
	answer.append([len(set_temp),len(temp)])

for i in range(len(answer)) :
	print(answer[i][0],answer[i][1])