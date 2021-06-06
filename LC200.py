class Solution:
    DIR = [(0,1),(1,0),(-1,0),(0,-1)]
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        len_col = len(grid[0])
        len_row = len(grid)
        def dfs(row, col):
            grid[row][col] = '-1';
            for dx, dy in self.DIR:
                if 0 <= row+dx < len_row and 0 <= col+dy < len_col:
                    if grid[row+dx][col+dy] == '1':
                        dfs(row+dx,col+dy)
                    
        count = 0
        
        for col in range(len_col):
            for row in range(len_row):
                if(grid[row][col] == '1'):
                    count += 1
                    dfs(row,col)
        
        return count
        
