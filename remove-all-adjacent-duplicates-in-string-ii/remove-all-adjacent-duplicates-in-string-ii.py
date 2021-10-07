class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lista = [['#',0]]
        for i in s:
            if lista[-1][0] == i:
                lista[-1][1]+=1
                if lista[-1][1] == k:
                    lista.pop()
            else:
                lista.append([i,1])
        return ''.join([s[0]*s[1] for s in lista[1:]])