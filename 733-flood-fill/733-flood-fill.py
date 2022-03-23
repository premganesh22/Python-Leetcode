class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def get_neighbors(r,c):
            neighbors = [[-1,0],[1,0],[0,-1],[0,1]]
            result = []
            for nr,nc in neighbors:
                row = nr+r
                col = nc+c
                if row in range(0,len(image)) and col in range(0,len(image[0])):
                    result.append((row,col))
            return result
        def BFS(row,col,new_color):
            old_color = image[row][col]
            image[row][col] = new_color
            queue = deque()
            queue.append((row,col))
            while queue:
                r,c = queue.popleft()
                for nr,nc in get_neighbors(r,c):
                    if image[nr][nc] == old_color:
                        image[nr][nc] = new_color
                        queue.append((nr,nc))

        if newColor == image[sr][sc]:
            return image
        row = len(image)
        col = len(image[0])
        BFS(sr, sc, newColor)
        return image
