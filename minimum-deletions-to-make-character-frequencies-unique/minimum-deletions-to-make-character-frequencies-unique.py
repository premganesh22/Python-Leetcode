class Solution:
    def minDeletions(self, s: str) -> int:
        maps = defaultdict(int)
        for i in s:
            maps[i]+=1

        
        count = 0
        array = set()
        for key,freq in maps.items():
            while freq>0 and freq in array:
                freq-=1
                count+=1
            array.add(freq)
        return count