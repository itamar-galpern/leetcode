"""Idea: Binary search over the weight, similiar to Koko eating bananas"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        while low < high:
            mid = low + (high-low)//2
            if self.canShip(weights, days, mid):
                high = mid
            else:
                low = mid+1
        return low


    def canShip(self, weights, days, weight):
        count, index = 0, 0
        while count < days:
            load = 0
            while index < len(weights):
                if load + weights[index] <= weight:
                    load += weights[index]
                    index += 1
                else:
                    break
            count += 1
            if index == len(weights):
                return True
        return False
                
            


        