class Solution:
    def customSortString(self, order: str, s: str) -> str:
        #Create dic with all char in S
        s_dic = {}
        for i in s:
            s_dic[i] = s_dic.get(i,0)+1
        
        
        ans = []
        
        for i in order:
            if i in s_dic:
                ans.append(i*s_dic[i])
                s_dic[i] = 0
        
        for key, val in s_dic.items():
            if val:
                ans.append(key*val)
        
        return "".join(ans)