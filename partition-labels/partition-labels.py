class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        for i in range(len(s)):
            dic[s[i]] = i

        start,end = 0, 0
        output = []
        for i in range(len(s)):
            end = max(end,dic[s[i]])
            if i == end:
                output.append(end-start+1)
                start = end+1
        return output
        