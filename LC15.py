from itertools import combinations
import math

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def twoSum(nums: List[int], target: int):
            hashset = set()
            res = set()
            
            for num in nums:
                if target - num in hashset:
                    res.add((target - num, num))
                hashset.add(num)
            
            return res
    
        if len(nums) < 3:
            return []

        res = set()
        
        for i in range(0, len(nums)-2):
            a = nums[i]
            nums_remaining = nums[i+1:]
            target_remaining = 0 - a
        
            for b, c in twoSum(nums_remaining, target_remaining):
                res.add((a,b,c))
        
        return res
