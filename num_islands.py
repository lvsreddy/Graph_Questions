# Number of island problem

def numofIslands(lst):
    r = len(lst)
    c = len(lst[0])
    island_count = 0
    for i in range(r):
        for j in range(c):
            if(lst[i][j] == 1):
                island_count += 1
                mark_island(lst, i, j ,r, c)
    return island_count

def mark_island(lst, i, j ,r, c):
    if i<0 or i>=r or j<0 or j>=c or lst[i][j] == 0:
        return
    lst[i][j] = 0
    mark_island(lst, i-1, j ,r, c)
    mark_island(lst, i+1, j ,r, c)
    mark_island(lst, i, j-1 ,r, c)
    mark_island(lst, i, j+1 ,r, c)
    # if only four boundaries are considered i.e., diagonal 1's are not considered then remove the below four lines
    mark_island(lst, i-1, j-1 ,r, c)
    mark_island(lst, i+1, j+1 ,r, c)
    mark_island(lst, i+1, j-1 ,r, c)
    mark_island(lst, i-1, j+1 ,r, c)
    
lst = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

print(numofIslands(lst))
