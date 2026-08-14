class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [] 
        l = 0 
        r = 0
        dq = deque()

        while r < len(nums) :
            while dq and nums[dq[-1]] < nums[r] :
                dq.pop()
            dq.append(r)

            if l > dq[0]:
                dq.popleft()

            if (r+1) >= k :
                res.append(nums[dq[0]])
                l += 1 # why ?
            r += 1 # why ? 
        return res
