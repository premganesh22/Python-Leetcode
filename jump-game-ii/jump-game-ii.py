class Solution:
    def jump(self, lista: List[int]) -> int:
        l = r = 0
        res = 0
        while r < len(lista)-1:
            furthermost = 0

            for i in range(l,r+1):
                furthermost = max(furthermost,i+lista[i])

            l = r+1
            r = furthermost
            res+=1
        return res
        