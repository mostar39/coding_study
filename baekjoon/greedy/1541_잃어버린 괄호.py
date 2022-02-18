input_data = input()

new_input = ''
first_minus = 0
for i in range(len(input_data)) :
	if i == 0 :
		new_input = input_data[i]+new_input
	elif (i == len(input_data)-1) & (first_minus==1):
		new_input = new_input+input_data[i]+')'
	elif (input_data[i] == '-') & (first_minus==0):
		first_minus = 1
		new_input = new_input + '-('
	elif (input_data[i] == '-') & (first_minus==1) :
		new_input = new_input+')-'
		first_minus = 0
	else :
		new_input = new_input + input_data[i]

minus_list = new_input.split('-')

all_thing = 0
for i in range(len(minus_list)) :
	minus_list[i] = minus_list[i].replace('(','')
	minus_list[i] = minus_list[i].replace(')','')
	plus_list = minus_list[i].split('+')
	temp_plus = 0
	for j in range(len(plus_list)) :
		temp_plus += int(plus_list[j])
	if i == 0 :
		all_thing = temp_plus
	else :
		all_thing = all_thing - temp_plus

print(all_thing)
