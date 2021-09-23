class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        max_freq = 0
        for i in tasks:
            dic[i] = dic.get(i,0)+1
            max_freq = max(max_freq,dic[i])
        
        count_freq = 0
        for k,v in dic.items():
            if v == max_freq:
                count_freq+=1
        return max(len(tasks),(max_freq-1)*(n+1) + count_freq)
        
        