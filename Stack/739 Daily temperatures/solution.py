"""
0739. Daily Temperatures (Medium)
https://leetcode.com/problems/daily-temperatures/
Solved 2026-08-31 | <20 min | unaided
Time O(n) / Space O(n)
"""

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    return_arr = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            _, idx = stack.pop()
            return_arr[idx] = i - idx
        stack.append((temp, i))
    return return_arr
                        
if __name__ == "__main__":
    assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    assert dailyTemperatures([30,60,90]) == [1,1,0]
    assert dailyTemperatures([90,60,30]) == [0,0,0]
    print("ok")
