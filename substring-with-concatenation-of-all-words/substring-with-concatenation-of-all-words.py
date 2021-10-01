class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        dic = {}
        for i in words:
            dic[i] = dic.get(i,0)+1

        wordLen = len(words)
        wordsize = len(words[0])
        output = []
        for i in range(0,len(s)-wordLen*wordsize+1):
            seen = {}
            for j in range(wordLen):
                workindex = i+j*wordsize
                subStr = s[workindex:workindex+wordsize]
                if subStr not in dic:

                    break
                seen[subStr] = seen.get(subStr,0)+1
                if seen[subStr] > dic[subStr]:

                    break
                if j+1 == wordLen:
                    output.append(i)
        return output
        