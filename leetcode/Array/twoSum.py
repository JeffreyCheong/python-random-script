
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        needs = {}

        for i in range(len(nums)):

            if target - nums[i] in needs:
                return [needs[target-nums[i]], i]

            else:
                needs[nums[i]] = i

if __name__ == '__main__':
    sol = Solution()
    nums=[2, 7, 11, 15]
    nums.reverse()
    print(nums)
    target=9
    print(sol.twoSum(nums=nums, target=target))