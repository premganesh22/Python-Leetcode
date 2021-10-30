class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next, self.prev = None, None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0) #Less frequently used
        self.right = Node(0,0) #Most frequently used
        self.left.next, self.right.prev = self.right,self.left
    
    def remove(self,node):
        nxt,prev = node.next,node.prev
        prev.next, nxt.prev = nxt, prev
        
    def insert(self,node):
        nxt,prev = self.right, self.right.prev
        self.right.prev = node
        prev.next = node
        node.next,node.prev = nxt,prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            
            return self.cache[key].value
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)