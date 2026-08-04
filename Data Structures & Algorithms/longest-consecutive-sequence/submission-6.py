class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:
            streak, curr = 0, num
            while curr in numSet : 
                curr += 1
                streak += 1
            longest = max(longest, streak)
        return longest 





