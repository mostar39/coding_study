# 배열에 있는 수를 M번 더했을 때, 최대가 되도록 하여라
# 단 한 인덱스에 대해 K번만큼만 반복될 수 있다
# 배열의 크기는 N 이다

N, M, K = map(int,input().split())
list_num = list(map(int, input().split()))

assert len(list_num) == N

list_num.sort()

max_num = list_num[len(list_num)-1]
second_max_num = list_num[len(list_num)-2]

circle = M // (K + 1)
namuji = M%(K + 1)

print(max_num*circle*K + second_max_num*circle + namuji*max_num)