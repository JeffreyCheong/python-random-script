
"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

from typing import List
from functools import reduce
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]

        for i in range(1, len(output)):
            output[i] = output[i-1] * nums[i-1]
        
        R = 1
        for i in range(len(output) - 1, -1, -1):
            output[i] = output[i]*R
            R *=nums[i]

        return output


    def secondarySolution(self, nums: List[int]) -> List[int]:
        
        arr = []
        temp = 0
        for i in nums:
            temp = i

            if temp == 0:
                arr.append(i)
                if len(arr) > 1:
                    return [0 for i in range(len(nums))]

        arr = []
        for i in range(0, len(nums)):
            newList = nums[:]
            newList.pop(i)
            tempNums = newList
            arr.append(self.listMultiplier(arr=tempNums))
        return arr

    def listMultiplier(self, arr):
        return 1* reduce(lambda x, y: x * y, arr, 1)


if __name__ == '__main__':
    nums = [-1,-1,1,-1,-1 ]

    sol = Solution()

    res = sol.productExceptSelf(nums=nums)
    print(res)
    # very slow solutions
    result = sol.secondarySolution(nums=nums)
    print(result)