class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-97]+=1
            dic[tuple(count)].append(i)
        output = []
        for key,values in dic.items():
            output.append(values)
        return output
        