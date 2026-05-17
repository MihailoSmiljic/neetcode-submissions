class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for zag in s:
            if zag == '(' or zag == '[' or zag == '{' :
                stack.append(zag)
                continue

            if zag == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
                continue
            elif zag == '}' and len(stack) > 0 and stack[-1] == '{':
                stack.pop()
                continue
            
            elif zag == ']' and len(stack) > 0 and stack[-1] == '[':
                stack.pop()
                continue

            else:
                return False
                        

        if len(stack) == 0:    
            return True
        return False