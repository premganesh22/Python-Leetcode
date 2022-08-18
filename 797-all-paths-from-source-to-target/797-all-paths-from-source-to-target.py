class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adj_list = {}
        for i in range(len(graph)):
            adj_list[i] = graph[i]

        output = []
        global_output = []

        def dfs(node):
            global_output.append(node)
            for nei in adj_list[node]:
                dfs(nei)
            if node == len(graph)-1:
                output.append(global_output[:])
            global_output.pop()


        global_output.append(0)
        for i in adj_list[0]:
            dfs(i)
        
        return output