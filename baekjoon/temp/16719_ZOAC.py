def solution(s,start) :
	global answer

	if not s :
		return

	target = min(s)
	idx = s.index(target)

	answer[start + idx] = target
	print("".join(answer))

	solution(s[idx+1:], start+idx+1)
	solution(s[:idx], start)

word = list(map(str,input().strip()))
answer = ['']*len(word)
solution(word,0)