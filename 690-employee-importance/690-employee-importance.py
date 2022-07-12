"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        hash_map = {}
        for emp in employees:
            hash_map[emp.id] = {'imp': emp.importance, 'sub': emp.subordinates}
        
        global_output = [0]
        def dfs(id):
            global_output[0]+=hash_map[id]['imp']
            for i in hash_map[id]['sub']:
                dfs(i)
        dfs(id)
        
        return global_output[0]
        
                
            
        
        
        