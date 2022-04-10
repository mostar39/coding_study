import sys

n = int(sys.stdin.readline())
start, end = 1, 10**400

while True :
    if start>end :
        break
    mid = (start + end) // 2
    if mid*mid == n :
        print(mid)
        break
    elif mid*mid > n :
        end = mid-1
    elif mid*mid < n :
        start = mid+1