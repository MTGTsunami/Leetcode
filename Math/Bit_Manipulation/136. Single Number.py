"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        count = {v : k for k, v in count.items()}
        return count[1]


class Solution2:
    # O(1) space
    def singleNumber(self, nums: List[int]) -> int:
        x = nums[0]
        for i in nums[1:]:
            x ^= i
        return x
