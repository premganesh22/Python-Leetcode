class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def get_neighbors(r,c):
            neighbors = [[-1,0],[1,0],[0,-1],[0,1]]
            result = []
            for nr,nc in neighbors:
                row = nr+r
                col = nc+c
                if row in range(0,len(grid)) and col in range(0,len(grid[0])):
                    result.append((row,col))
            return result

        def BFS(r,c):
            queue = deque()
            queue.append((r,c))
            grid[r][c] = '0'
            while queue:
                r,c = queue.popleft()
                for row,col in get_neighbors(r,c):
                    if grid[row][col] == '1':
                        queue.append((row,col))
                        grid[row][col] = '0'



        island = 0
        row = len(grid)
        col = len(grid[0])
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    island+=1
                    BFS(r,c)
        return island
        