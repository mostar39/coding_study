import sys


n, m, circle_how_many = map(int,sys.stdin.readline().split())
array = [list(map(int,sys.stdin.readline().split())) for i in range(n)]


def circle(temp, min_row, min_col, max_row, max_col) :
    for i in range(min_row,max_row+1) :
        if i==min_row or i==max_row :
            j_list = range(min_col,max_col+1)
        else :
            j_list = [min_col, max_col]
        for j in j_list :
            if i == min_row and j != max_col :
                temp[i][j] = array[i][j+1]
            elif i > min_row and j == min_col :
                temp[i][j] = array[i-1][j]
            elif i == max_row and j != min_col :
                temp[i][j] = array[i][j-1]
            elif i < max_row and j== max_col :
                temp[i][j] = array[i+1][j]
    return temp

circle_num = min(n,m) // 2
for i in range(circle_how_many) :
    min_row = 0
    min_col = 0
    max_row = n-1
    max_col = m-1
    temp = [[0]*m for _ in range(n)]
    for j in range(circle_num) :
        temp = list(circle(temp,min_row, min_col, max_row, max_col))
        min_row += 1
        min_col += 1
        max_row -= 1
        max_col -= 1
    array = list(temp)

for i in range(len(array)) :
    print(*array[i])

