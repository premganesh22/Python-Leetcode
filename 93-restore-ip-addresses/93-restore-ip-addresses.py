class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def helper(s,idx,slate,result):
            #Constrains
            if slate:
                if len(slate) > 4:
                    return
                if len(slate[-1]) > 1 and slate[-1][0] == '0':
                    return
                if int(slate[-1]) not in range(0,256):
                    return
            #Base
            if idx == len(s) and len(slate) == 4:
                result.append('.'.join(slate[:]))
            else:
                for i in range(idx,len(s)):
                    slate.append(s[idx:i+1])
                    helper(s,i+1,slate,result)
                    slate.pop()
                return result  
        return helper(s,0,[],[])
        