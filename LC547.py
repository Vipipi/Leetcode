class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        parent = dict()
        m = len(M)
        n = len(M[0])
        
            
        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] != x:
                parent[x] = find(parent[x])
                
            return parent[x]
        
        groups = len(M)
        
        for i in range(m):
            for j in range(i+1, n):
                if M[i][j] == 1:
                    p1, p2 = find(i), find(j)
                    
                    if p1 != p2:
                        groups -= 1

                    parent[p1] = p2
                
                
        return groups
