from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        adj_list = defaultdict(list)
        backward_edge = defaultdict(list)
        in_degree = {node: 0 for node in range(1,n+1)}
        time_to_complete = [0] * (n+1)
        for prevC, nextC in relations:
            adj_list[prevC].append(nextC)
            backward_edge[nextC].append(prevC)
            in_degree[nextC] += 1
        stack = [i for i in range(1,n+1) if i not in backward_edge]
        while stack:
            current = stack.pop()
            adj = backward_edge.get(current, None)
            time_to_complete[current] = time[current-1]
            if adj:
                time_to_complete[current] += max([time_to_complete[i] for i in adj])
            for next_course in adj_list[current]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    stack.append(next_course)
        return max(time_to_complete)

