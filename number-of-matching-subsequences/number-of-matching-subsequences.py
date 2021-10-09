class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dic = defaultdict(list)
        for i in words:
            dic[i[0]].append(i)
        count = 0
        for char in s:
            words_in_char = dic[char]
            dic[char] = []
            for c in words_in_char:
                if len(c) == 1:
                    count+=1
                else:
                    dic[c[1]].append(c[1:])
        return count