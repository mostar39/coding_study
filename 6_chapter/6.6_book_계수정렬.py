# 모든 데이터 양의 정수
# 데이터의 차이가 1,000,000을 넘지 않을 때 효과적
# 왜 Why ? 계수 정렬을 이용할 때에는 '모든 범위를 담을 수 있는 크기의 리스트'를 선언해야하기 때문임
# if (max-min == 100) 이면, 리스트 크기를 101로 초기화해줘야 함
# 비교기반 알고리즘이 아님

# 데이터의 범위가 한정되어있고, 동일한 값을 가지는 데이터가 여러개 일 때 효과적임

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
count = [0] * (max(array)+1)

for i in range(len(array)) :
	count[array[i]] += 1

for i in range(len(count)) :
	for j in range(count[i]) :
		print(i, end=' ')