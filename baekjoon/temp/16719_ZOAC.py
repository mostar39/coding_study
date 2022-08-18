def dfs(start, what) :
	if not what :
		return

	min_new_str = what.index(min(what))
	answer[start + min_new_str] = str_[start+min_new_str]

	print(''.join(answer))

	dfs(start+min_new_str+1, what[min_new_str+1:])
	dfs(start, what[:min_new_str])



str_ = input().strip()
answer = [''] * len(str_)

dfs(0,str_)