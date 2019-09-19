"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


class Backtracking_Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        summ = sum(nums)
        if summ % 2 != 0:
            return False

        nums.sort(reverse=True)
        target = [summ / 2] * 2

        def dfs(idx):
            if idx == len(nums):
                return True

            for i in range(2):
                if target[i] >= nums[idx]:
                    target[i] -= nums[idx]
                    if dfs(idx + 1):
                        return True
                    target[i] += nums[idx]
            return False

        return dfs(0)


class DP_Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        summ = 0
        for num in nums:
            summ += num
        if summ % 2 != 0:
            return False
        summ //= 2

        dp = [[False for _ in range(summ + 1)] for _ in range(len(nums) + 1)]
        for j in range(summ + 1):
            dp[0][j] = False
        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, summ + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]
