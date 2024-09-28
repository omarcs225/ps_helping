class Solution:
    def evalRPN(self, tokens) -> int:
        
        lst = []
        for item in tokens:
            if item == '+' or item == '-' or item == '*' or item == '/':
                
                second = lst.pop()
                first = lst.pop()
                
                if item == '+':
                    lst.append(first+second)
                elif item == '-':
                    lst.append(first-second)
                elif item == '*':
                    lst.append(first*second)
                else:
                    lst.append(int(first/second))
            else:
                lst.append(int(item))
        
        return round(lst.pop())

