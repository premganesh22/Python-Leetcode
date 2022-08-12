class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        change = {}
        for index in range(len(indices)):
            length = len(sources[index])
            if s[indices[index]:indices[index]+length] == sources[index]:
                change[indices[index]] = {'targets':targets[index], 'end':indices[index]+length}
            
        output = ''
        start = 0
        end = len(s)-1
        
        while start <= end:
            if start in change:
                output+=change[start]['targets']
                start = change[start]['end']
            else:
                output+=s[start]
                start+=1
        
        return output