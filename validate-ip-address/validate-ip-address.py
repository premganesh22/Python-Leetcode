class Solution(object):
    
    def validate_ipv4(self,address):
        split = address.split('.')
        if len(split) != 4:
            return 'Neither'
        try:
            for i in split:
                if str(int(i)) != i or not (0 <= int(i) <= 255):
                    return 'Neither'
            return 'IPv4'
        except:
            return 'Neither'
        
    def validate_ipv6(self,address):
        split = address.split(':')
        if len(split) != 8:
            return 'Neither'
        try:
            for i in split:
              
                if not (len(i) <= 4 and int(i,16) >= 0):
                    return 'Neither'
            return 'IPv6'
        except:
            return 'Neither'
                    
            
        
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            return self.validate_ipv4(IP)
        return self.validate_ipv6(IP)
        