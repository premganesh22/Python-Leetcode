class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
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
            land = 1
            queue = deque()
            queue.append((r,c))
            grid[r][c] = 0
            while queue:
                r,c = queue.popleft()
                #print(get_neighbors(r,c))
                for row,col in get_neighbors(r,c):
                    if grid[row][col] == 1:
                        land+=1
                        queue.append((row,col))
                        grid[row][col] = 0
            return land


        island = 0
        row = len(grid)
        col = len(grid[0])
        max_land = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    island+=1
                    land = BFS(r,c)
                    max_land = max(max_land,land)
        return max_land
        