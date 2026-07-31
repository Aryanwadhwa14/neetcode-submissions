class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break 
            elif i > 0 and a == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums)-1

            while l < r: 
                t_sum = a + nums[l] + nums[r]
                if t_sum < 0 :
                    l += 1
                elif t_sum > 0 : 
                    r -= 1 
                else :
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    if nums[l] == nums[l-1]:
                        l += 1
        return res









                    

                


