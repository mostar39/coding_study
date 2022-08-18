from collections import deque
text = input().strip().split('<')[1:]
text_que = deque(text)
hey = ['main>', 'div', 'p']
end = ['/main>', '/div>', '/p>']
temp_for_p = ''

for i in range(len(text)):
	sign = 0
	pop_ = text_que.popleft()
	if ('main>' in pop_) and (pop_ != '/main>'):
		continue
	elif ('p>' in pop_) and (pop_ != '/p>') :
		p_list = pop_.split('>')
		if p_list[0]!= 'p' :
			p_list[0] = ''
			new_te = ''.join(p_list)
			temp_for_p += new_te
		else :
			temp_for_p += p_list[1]
	elif 'div title="' in pop_ :
		pop_ = pop_.replace('"','')
		p_list = pop_.split('=')
		print('title : '+ p_list[1][:-1].strip())
	elif pop_ in end :
		if '/p>' == pop_ :
			temp_temp_ = temp_for_p.split()
			temp_temp_temp =' '.join(temp_temp_)
			print(temp_temp_temp.strip())
			temp_for_p = ''
	elif '>' in pop_ :
		p_list = pop_.split('>')
		if p_list[0] not in hey :
			p_list[0] = ''
		new_te = ''.join(p_list)
		temp_for_p += new_te
