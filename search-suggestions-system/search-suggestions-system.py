class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        res = []
        prefix = ''
        for index, char in enumerate(searchWord):
            prefix+=char
            count = 0
            temp = []
            for p in products:
                if p[:index+1] == prefix:
                    count+=1
                    temp.append(p)
                if count == 3:
                    break
            res.append(temp)
        return res
            