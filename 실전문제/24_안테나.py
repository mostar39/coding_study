import sys

n = int(sys.stdin.readline())
array = list(set(map(int,sys.stdin.readline().split())))

array.sort()

print(array[(n-1)//2])