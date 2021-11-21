class Solution:
    def frequencySort(self, s: str) -> str:
        hash_map = defaultdict(int)
        for i in s:
            hash_map[i]+=1
        
        freq = sorted(hash_map.items(),key=lambda x:x[1], reverse=True)
        output = ''
        for value, time in freq:
            output+= value*time
        return output