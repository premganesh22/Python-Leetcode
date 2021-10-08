class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = defaultdict(list)
        for i in strs:
            dic[tuple(sorted(i))].append(i)
        output = []
        for k, v in dic.items():
            output.append(v)
        return output