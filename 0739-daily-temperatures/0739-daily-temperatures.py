class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answers = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack:
                curr_val, curr_index = stack.pop()
                if curr_val < temp:
                    answers[curr_index] = i - curr_index
                else:
                    stack.append((curr_val, curr_index))
                    break
            stack.append((temp, i))
        return answers
        