class Solution:
    def trap(self, height: List[int]) -> int:
        # leftmax
        # rightmax
        # water level -> min(leftmax, rightmax)
        # trapped water = water level - height[i]
        res = 0 
        for i in range(len(height)):
            leftmax = rightmax = height[i]
            for j in range(i+1):
                leftmax = max(leftmax, height[j])
            for j in range(i, len(height)):
                rightmax = max(rightmax, height[j])
            
            res += min(leftmax, rightmax) - height[i]
    

        return res 