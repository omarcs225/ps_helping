class Solution:
    def reverse(self, num) :
        
        flag_neg = False
        
        if num<0:
            flag_neg = True
            num = -num
        
        ln = 0
        curr = num
        
        while curr:
            ln+=1
            curr //=10
            
        count = ln-1
        res = 0
        
        while num:
            n = num % 10
            res += n*(10**count)
            count-=1
            num //=10
            
        if res>(2**31 - 1) or res<(-2**31):
            return 0
        
        return res if not flag_neg else -res

