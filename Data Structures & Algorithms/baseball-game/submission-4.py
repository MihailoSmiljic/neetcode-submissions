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
                    sum+=stack[len(stack)-1]
            elif i == "C":
                sum-=stack[len(stack)-1]
                stack.pop()
            elif i == "D":
                if len(stack) < 1:
                    continue
                stack.append(stack[len(stack)-1] * 2)
                sum+=stack[len(stack)-1]
            else:
                stack.append(int(i))
                sum+=int(i)


        return sum