class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0 
        res = []    
        for r in range(len(nums)):
            if (r-l+1) == k :
                mp = max(nums[l:r+1])
                res.append(mp)
                l += 1
        return res