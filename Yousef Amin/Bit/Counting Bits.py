class Solution:
    def countBits(self, n) :
        return [ self.decimalToBinary(i).count('1') for i in range(n+1)]
    
    def decimalToBinary(self,n): 
        return bin(n).replace("0b", "") 

