class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Build Adjacency list
        a_list = {}
        for target, source in prerequisites:
            if source in a_list:
                a_list[source].append(target)
            else:
                a_list[source] = [target]
            
        visited = set()
        arrived = set()
        departed = set()
        def dfs(course):
            visited.add(course)
            arrived.add(course)
            if course in a_list:
                for nei in a_list[course]:
                    if nei not in visited:
                        if not dfs(nei):
                            return False
                    elif nei not in departed:
                        return False

            departed.add(course)
            return True
        
        for course in a_list:
            if course not in visited:
                if not dfs(course):
                    return False
                
        return True
            