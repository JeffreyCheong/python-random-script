"""

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""

from typing import List
from time import time
class Solution:

    def containsDuplicate(self, num: List[int]) -> bool:

        for i in nums:
            if nums.count(i) > 1:
                return True

        return False

    def containDuplicateFastest(self, num: List[int]) -> bool:

        if len(num) != len(set(num)):
            return True

        return False


if __name__ == "__main__":

    sol = Solution()
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,1]

    # nums = [1,2,3,1]
    startTime = time()
    sol1 = sol.containsDuplicate(num = nums)
    if sol1:
        endTime = time()
        totalTime = endTime - startTime
        print('sol totalTime = {}'.format(totalTime))

    startTime2 = time()
    sol2 = sol.containDuplicateFastest(num = nums)

    if sol2:
        endTime2 = time()
        totalTime2 = endTime2 - startTime2
        print('sol2 totalTime = {}'.format(totalTime2))
    

