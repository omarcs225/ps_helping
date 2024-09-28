class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        stack = []
        res = [0]*len(temperatures)
        
        for index,temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                days = index - stack[-1][1]
                res[stack[-1][1]] = days
                stack.pop()
            stack.append((temp,index))
        
        return res        