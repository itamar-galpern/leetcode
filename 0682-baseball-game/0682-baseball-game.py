class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for element in operations:
            if element == '+':
                if not stack or not stack[-2]:
                    raise ValueError("Not enough values")
                stack.append(stack[-1] + stack[-2])
            elif element == 'D':
                if not stack:
                    raise ValueError("Can not double, stack is empty")
                stack.append(2*stack[-1])
            elif element == 'C':
                if not stack:
                    raise IndexError("Stack is empty")
                stack.pop()
            else:
                stack.append(int(element))
        return sum(stack)
        