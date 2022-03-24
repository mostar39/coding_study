import heapq
import sys
#=====================================ming=========================================
n, m =map(int,sys.stdin.readline().split())

array = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
max_gram = [int(sys.stdin.readline().strip()) for i in range(m)]

array_price = sorted(array,reverse=True ,key=lambda x:x[1])
max_gram.sort()

plus = 0
for i in range(len(max_gram)) :
	for j in range(len(array_price)) :
		if array_price[j][0] <= max_gram[i] :
			plus += array_price[j][1]
			del array_price[j]
			break
print(plus)

#===============================구글링==============================================
# Heap은 최댓갑 및 최솟값을 찾아내는 연산을 빨리하기 위해서 고안된 완전이진트리기반 자료구조
# A가 B의 부모노드이면, A의 key값과 B의 key값 사이에는 대소관계가 성립함
# 키 값의 대소관계는 부모/자식 간에만 성립하고, 형제노드 사이에는 대소 관계가 정해지지 않음

# 최대 힙 : 부모 노드의 키 값이 자식노드의 키 값보다 항상 큰 힙
# 최소 힙 : 부모 노드의 키 값이 자식노드의 키 값보다 항상 작은 힙

# 0번 인덱스는 사용되지 않음
# 왼쪽 자식의 인덱스 = (부모) * 2
# 오른쪽 자식의 인덱스 = (부모) * 2 + 1
# 부모의 인덱스 = (자식) / 2

# 힙의 삽입 : 새로운 요소를 마지막 노드에 이어서 삽입 후 힙의 성질을 만족할 때까지 부모 노드의 교환
# 힙의 삭제 : (최대 힙) 루트 ㄴ트 삭제 후 마지막 노드를 루트 노드에 위치 시킨 뒤 힙의 성질을 만족할 때까지 자식노드와 교환


heap_items = [1,3,5,7,9]
max_heap = []
for item in heap_items :
	heapq.heappush(max_heap, (-item, item))
print(max_heap)
