class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        
        if not s:
            return 0

        sign = 1
        index = 0
        
        if s[0] in ['-','+']:  # Check for sign
            if s[0] == '-':
                sign = -1
            index += 1

        num = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            if num > (2**31 - 1) // 10 or (num == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31
            
            num = num * 10 + digit
            index += 1
        
        return sign * num
