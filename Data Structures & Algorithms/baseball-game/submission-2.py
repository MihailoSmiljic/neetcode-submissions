class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        sum = 0
         
        for i in operations:
            if i == "+":
                if len(stack) < 2:
                    continue 
                else:
                    stack.append(stack[len(stack)-1] + stack[len(stack)-2])
            elif i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[len(stack)-1] * 2)
            else:
                stack.append(int(i))
        for i in stack:
            sum += i
        return sum