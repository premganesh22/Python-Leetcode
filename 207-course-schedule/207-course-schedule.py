class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        for cor, pre in prerequisites:
            adj_list[pre].append(cor)

        visited = [-1]*numCourses
        arrival = [-1]*numCourses
        departure = [-1]*numCourses

        timestamp = [0]

#         def dfs(node):
#             visited[node] = 1
#             arrival[node] = global_time[0]
#             global_time[0]+=1
                
#             for nei in adj_list[node]:
#                 if visited[nei] == -1:
#                     if not dfs(nei):
#                         return False
#                 else:
#                     if departure[node] == -1:
#                         return False

#             departure[node] = global_time[0]
#             global_time[0]+=1
#             return True

        def dfs(s):

            arrival[s] = timestamp[0]
            timestamp[0]+=1
            visited[s] = 1
            for edge in adj_list[s]:
                if visited[edge] == -1:
                    if not dfs(edge):
                        return False
                else:
                    if departure[edge] == -1:
                        return False
            departure[s] = timestamp[0]
            timestamp[0]+=1
            return True


        for node in range(numCourses):
            if visited[node] == -1:
                if not dfs(node):
                    return False
        return True