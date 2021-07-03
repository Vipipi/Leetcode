class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(x, y):
            if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                board[x][y] = "N"
                for dx, dy in DIR:
                    dfs(x+dx, y+dy)
        
        for dm in range(m):
            dfs(dm,0)
            dfs(dm,n-1)
            
        for dn in range(1, n-1):
            dfs(0, dn)
            dfs(m-1, dn)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "N":
                    board[i][j] = "O"
                    
        
