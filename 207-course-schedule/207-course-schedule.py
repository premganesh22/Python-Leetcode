class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Build Adjacency list
        a_map = {}
        for c, d in prerequisites:
            if d in a_map:
                a_map[d].append(c)
            else:
                a_map[d] = [c]
        
        
        arrival = set()
        visited = set()
        departure = set()
        global_status = [True]
        def dfs(node):
            
            arrival.add(node)
            visited.add(node)
            if node in a_map:
                for course in a_map[node]:
                    if course not in visited:
                        dfs(course)

                    else:
                        if course not in departure:
                            global_status[0] = False

            departure.add(node)
            
        for node in a_map:
            if node not in visited:
                dfs(node)
        return global_status[0]
                    
        
        