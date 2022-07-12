class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def get_neigbhours(node):
            direction = [[0,1], [0,-1], [1, 0], [-1,0]]
            output = []
            for x,y in direction:
                if 0 <= node[0]+x < len(grid) and 0<= node[1]+y < len(grid[0]) and grid[node[0]+x][node[1]+y] == 1:
                    output.append((node[0]+x, node[1]+y))
            return output
        
        def dfs(node):
            visited.add(node)
            global_count[0]+=1
            for nei in get_neigbhours(node):
                if nei not in visited:
                    dfs(nei)
                    
        global_count = [0]
        max_island = 0
        visited = set()
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if (m,n) not in visited and grid[m][n] == 1:
                    global_count = [0]
                    dfs((m,n))
                    max_island = max(max_island, global_count[0])
        return max_island