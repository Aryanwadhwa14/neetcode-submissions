class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {} 
        for i, j in enumerate(numbers):
            diff = target - j 
            if diff in seen :
                return [diff, j]
            seen[j] = i
        return 
            
