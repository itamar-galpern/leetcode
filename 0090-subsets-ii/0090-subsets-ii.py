class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        curr_subset, subsets = [], [[]]
        nums.sort()
        self.all_subsets(0, curr_subset, subsets, nums)
        return subsets
        
    def all_subsets(self, index, subset, subsets, nums):
        if index == len(nums):
            return
        subset.append(nums[index])
        subsets.append(subset[:])
        self.all_subsets(index+1, subset, subsets, nums)
        subset.pop()
        while index < len(nums)-1 and nums[index] == nums[index+1]:
            index += 1
        self.all_subsets(index+1, subset, subsets, nums)
        
        