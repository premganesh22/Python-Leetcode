class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        lista = [0]*60
        for i in time:
            lista[i%60]+=1
        for i in range(1,30):
            count+=lista[i]*lista[60-i]
        
        count+=(lista[0]*(lista[0]-1))//2
        count+=(lista[30]*(lista[30]-1))//2
        return count