class Solution:
    def maxArea(self, heights: List[int]) -> int:
        total = 0 
        for i in range(len(heights)):
            for j in range(i+1, len(heights)): # brute force
                width = j - i
                height = min(heights[i], heights[j])
                area = height * width 
                total = max(total, area)

        return total