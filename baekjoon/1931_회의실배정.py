n = int(input())
start_time_list = []
end_time_list = []
duration_list = []

for i in range(n):
	temp = list(map(int, input().split()))
	start_time_list.append(temp[0])
	end_time_list.append(temp[1])
	duration_list.append(temp[1]-temp[0])

max_time = max(end_time_list)
min_time = min(start_time_list)
time_list = [0] * (max_time-min_time)

count = 0
for i in range(n) :
	dur_min = min(duration_list)
	dur_min_index = duration_list.index(dur_min)

	if end_time_list[dur_min_index]-start_time_list[dur_min_index]==0 :
		count = count + 1
		duration_list[dur_min_index] = 99999999
		continue

	start_time_index = start_time_list[dur_min_index]-min_time
	end_time_index = end_time_list[dur_min_index]-min_time-1
	if time_list[start_time_index]==0 and (start_time_index == end_time_index) :
		time_list[start_time_index]=1
		count = count + 1
	else :
		its_ok = 0
		for i in range(end_time_index-start_time_index+1) :
			if time_list[start_time_index+i] == 0 :
				its_ok = its_ok+1
			else:
				continue
		if its_ok == end_time_index-start_time_index+1 :
			for i in range(end_time_index-start_time_index+1) :
				time_list[start_time_index+i] = 1
			count = count + 1
	duration_list[dur_min_index] = 99999999


print(count)

