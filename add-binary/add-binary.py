class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        count = []
        carry = 0
        i = 0
        a = a[::-1]
        b = b[::-1]
        print(a,b)
        while i < len(a) or i < len(b) or carry:
            if i<len(a):
                carry+=int(a[i])
            if i<len(b):
                carry+=int(b[i])
            count.append(str(carry%2))
            carry = carry//2
            i+=1

        return ''.join(count[::-1])