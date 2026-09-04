"""
0150. Evaluate Reverse Polish Notation (Medium)
https://leetcode.com/problems/evaluate-reverse-polish-notation/
Solved 2026-09-01 | <25 min | unaided
Time O(n) / Space O(n)
Notes: notes.md
"""

valid_operators = {"+": lambda x,y:y+x, "-": lambda x,y:y-x,
                    "*": lambda x,y:y*x, "/": lambda x,y: int(y/x)}

def evalRPN(tokens: list[str]) -> int:
    stack = []
    for token in tokens:
        if token in valid_operators:
            if len(stack) < 2:
                raise ValueError("Invalid action")
            x, y = stack.pop(), stack.pop()
            stack.append(valid_operators[token](x,y))
            continue
        stack.append(int(token))
    if stack:
        return stack[0]
    raise ValueError("Empty stack")

if __name__ == "__main__":
    assert evalRPN(["2","1","+","3","*"]) == 9
    assert evalRPN(["4","13","5","/","+"]) == 6
    assert evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    print("ok")

        