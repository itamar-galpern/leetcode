class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        permutations = [[]]
        
        for n in nums:
            curr = []
            for p in permutations:
                for i in range(len(p)+1):
                    cp = p.copy()
                    cp.insert(i, n)
                    curr.append(cp)
            permutations = curr
        return permutations