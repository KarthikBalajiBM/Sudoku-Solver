grid = [
    [0, 0, 7, 1, 4, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 5, 3],
    [2, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 6, 9, 0, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 4, 6],
    [0, 6, 0, 0, 0, 2, 1, 0, 0],
    [5, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 7, 0, 0, 5, 0, 9, 0, 0]
]


def show():
    for i in range(len(grid)):
        if i%3==0 and i!=0:
            print()
        for j in range(len(grid[0])):
            if j%3==0 and j!=0:
                print(" ",end=" ")
            print(grid[i][j],end=" ")
        
        print()

def check(row,col,num):
    if num in grid[row]:
        return False
    
    for i in range(len(grid)):
        if grid[i][col]==num:
            return False
    sub_grid_row=row-row%3
    sub_grid_col=col-col%3

    for i in range(sub_grid_row,sub_grid_row+3):
        for j in range(sub_grid_col,sub_grid_col+3):
            if grid[i][j]==num:
                # print(i,j)
                return False
    
    return True
# show()

def solve():
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j]==0:
            
                for num in range(1,10):
            
                    if check(i,j,num):
                        grid[i][j]=num
            
                        if solve():
                            return True
            
                        grid[i][j]=0
                return False
                    
    return True

solve()

show()
        
