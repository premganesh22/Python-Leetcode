class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def get_neighbours(m, n):
            output = []
            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                if 0 <= m+x < len(grid) and 0 <= n+y < len(grid[0]):
                    output.append((m+x, n+y))
            
            return output
        
        def BFS(node):
            
            queue = deque()
            queue.append(node)
            
            while queue:
                m, n = queue.popleft()
                grid[m][n] = "0"
                neighbours = get_neighbours(m, n)
                for x, y in neighbours:
                    if grid[x][y] == '1':
                        queue.append((x,y))
        
        def DFS(node):
            m, n = node[0], node[1]
            grid[m][n] = "0"
            neighbours = get_neighbours(m, n)
            for x, y in neighbours:
                if grid[x][y] == '1':
                    DFS((x,y))
            
        
        island= 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == '1':
                    island+=1
                    DFS((m,n))
        
        return island