class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        #Time: O(nlog(n))
        #Space: O(n)
        
        dic = {}
        for word in words:
            dic[word] = dic.get(word,0)+1
        
        '''
        Dictionary Solution
        '''
        #sorted_list = sorted(dic, key = lambda word: (-dic[word],word))
        #return sorted_list[:k]
    
        '''
        Heap solution
        '''
        heap = []
        for key,val in dic.items():
            #Converting value to negative since python default supports min heap
            heapq.heappush(heap,[-val,key])
        return [heapq.heappop(heap)[1] for i in range(k)]
        