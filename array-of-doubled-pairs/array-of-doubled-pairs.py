class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            dic[i] = dic.get(i,0)+1
        
        arr = sorted(arr)
        for i in arr:
            #print(dic,i)
            if dic[i]:
                if i < 0:
                    if i/2 in dic and dic[i/2]:
                        dic[i/2]-=1
                        dic[i]-=1
                    else:
                        return False
                else:
                    if i*2 in dic and dic[i*2]:
                        dic[i*2]-=1
                        dic[i]-=1
                    else:
                        return False
        return True