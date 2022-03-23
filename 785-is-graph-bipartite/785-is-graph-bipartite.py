class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def graph_biparity(graph):
            node_count = len(graph)
            visited = [-1]*node_count
            distance = [-1]*node_count

            def BFS(s):
                queue = deque()
                queue.append(s)
                visited[s] = 1
                distance[s]+=1
                while queue:
                    node = queue.popleft()
                    for edge in graph[node]:
                        if visited[edge] == -1:
                            visited[edge] = 1
                            distance[edge]=distance[node]+1
                            queue.append(edge)
                        else:
                            #print(edge,distance[edge],node,distance[node])
                            if distance[edge] == distance[node]:
                                return False
                return True

            for source in range(node_count):
                if visited[source] == -1:
                    if not BFS(source):
                        return False
            return True
        return graph_biparity(graph)
        