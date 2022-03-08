class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pali(s,idx,i):
            return s[idx:i+1] == s[idx:i+1][::-1]

        def pali(s,idx,slate,result):
            if idx == len(s):
                temp = []
                x = 0
                for index in slate:
                    temp.append(s[x:index+1])
                    x = index+1
                result.append(temp[:])
                return
            else:
                for i in range(idx,len(s)):
                    if is_pali(s,idx,i):
                        slate.append(i)
                        pali(s,i+1,slate,result)
                        slate.pop()
                return result


        return pali(s,0,[],[]) 
        