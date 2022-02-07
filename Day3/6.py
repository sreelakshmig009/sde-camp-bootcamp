def atoi(self,s):
        for i in s:
            if i.isalpha():
                return -1
        s_list = list(s.strip())
        if len(s_list) == 0: 
            return 0
        
        sign = -1 if s_list[0] == '-' else 1
        if s_list[0] in '-+' : 
            s_list = s_list[1:]
        ans = 0
        
        for symb in s_list:
            if not symb.isdigit(): 
                break
            ans = ans*10 + int(symb)
        
        return max(-2**31, min(sign*ans, 2**31-1))