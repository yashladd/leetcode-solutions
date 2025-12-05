class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def is_valid_ipv4(s: str) -> bool:
            parts = s.split('.')
            # IPv4 must have exactly 4 parts
            if len(parts) != 4:
                return False
            
            for part in parts:
                # 1. Check if part is empty or too long (max "255" is len 3)
                if not part or len(part) > 3:
                    return False
                # 2. Check if part contains non-digits
                if not part.isdigit():
                    return False
                # 3. Check for leading zeros (e.g., "01" is invalid, but "0" is valid)
                if len(part) > 1 and part[0] == '0':
                    return False
                # 4. Check range 0-255
                if not (0 <= int(part) <= 255):
                    return False
            return True

        def is_valid_ipv6(s: str) -> bool:
            parts = s.split(':')
            # IPv6 must have exactly 8 parts
            if len(parts) != 8:
                return False
            
            hexdigits = set("0123456789abcdefABCDEF")
            for part in parts:
                # 1. Check length (1 to 4 chars allowed)
                if not (1 <= len(part) <= 4):
                    return False
                # 2. Check if all characters are valid hex digits
                for char in part:
                    if char not in hexdigits:
                        return False
            return True

        # Main logic
        if '.' in queryIP:
            return "IPv4" if is_valid_ipv4(queryIP) else "Neither"
        elif ':' in queryIP:
            return "IPv6" if is_valid_ipv6(queryIP) else "Neither"
        else:
            return "Neither"