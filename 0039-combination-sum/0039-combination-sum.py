class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        current_path, all_paths = [], []
        candidates.sort()
        self.explore(candidates, target, current_path, all_paths, 0, 0)
        return all_paths

    def explore(self, candidates, target, path, all_paths, curr_sum, start):
        for i in range(start, len(candidates)):
            new_sum = curr_sum + candidates[i]
            if new_sum == target:
                all_paths.append(path + [candidates[i]])
                break
            elif new_sum > target:
                break
            else:
                path.append(candidates[i])
                self.explore(candidates, target, path, all_paths, new_sum,i)
                path.pop()
            