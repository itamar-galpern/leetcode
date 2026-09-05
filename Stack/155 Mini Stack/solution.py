"""
0155. Min Stack (Easy)
https://leetcode.com/problems/min-stack/
Solved 2026-08-31 | <5 min | unaided
Time O(1) complexity for all actions O(1) initalization
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
        self.stack.append(value)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
                        
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2
    print("ok")
