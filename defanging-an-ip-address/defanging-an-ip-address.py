class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        s = ''
        for i in address:
            if i != '.':
                s+=i
            else:
                s+='[.]'
        return s