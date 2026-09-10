'''
class Solution:
    def validIPAddress(self, IP) :
        def validIPv4(IP):
            parts = IP.split(".")
            for p in parts:
                    print (p in set(map(str, range(256))))
            x=(p in set(map(str, range(256))) for p in parts)
            print (list(x))
            return len(parts) == 4 and all(x)
            
        def validIPv6(IP):
            parts = IP.split(":")
            hexdigits = '0123456789abcdef'
            return len(parts) == 8 and all(0 < len(p) <= 4 and all(c.lower() in hexdigits for c in p) for p in parts)
        
        if validIPv4(IP): return "IPv4"
        if validIPv6(IP): return "IPv6"
        return "Neither"
'''
class Solution:
    def validIPAddress(self, IP) :
        """
        :type IP: str
        :rtype: str
        """
        
        res = 0
        ipv4 = IP.split('.')
        if len(ipv4) == 4:
            for x in ipv4:
                if x == '' or (x[0] == '0' and len(x) != 1) or not x.isdigit() or int(x) > 255:
                    res = 1
                    print (res)
                    break
            if not res:
                return 'IPv4'
        
        ipv6 = IP.split(':')
        hexdigits = '0123456789abcdef'
        if len(ipv6) == 8:
            for x in ipv6:
                if x == '' or len(x) > 4 or not all(c in hexdigits for c in x):
                    res = 1
                    break
            if not res:
                return 'IPv6'
        
        return 'Neither'   
    
print (Solution().validIPAddress('2001:0db8:85a3:0000:0000:8a2e:0370:7334'))