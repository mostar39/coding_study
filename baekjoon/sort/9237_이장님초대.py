import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

array.sort(reverse=True)
new_array = [(i+1)+array[i] for i in range(len(array))]
print(max(new_array)+1)