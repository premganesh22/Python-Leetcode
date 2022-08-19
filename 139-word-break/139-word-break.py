class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
                #Recursion
#         word_list = list(s)
#         dic_set  = set(wordDict)
        
#         def recursion(index):
#             if index == len(word_list):
#                 return True
#             for i in range(0,len(word_list)-index):
#                 if ''.join(word_list[index:(index+i+1)]) in dic_set:
#                     if recursion(index+i+1):
#                         return True
#             return False
#         return recursion(0)
        
        #DP
        table = [False]*(len(s)+1)
        table[0] = True
        wordDict = set(wordDict)
        for i in range(1,len(s)+1):
            for wordlength in range(1,i+1):
                if s[i-wordlength:i] in wordDict and table[i-wordlength]:
                    table[i] = True
                    break
        return table[len(s)]