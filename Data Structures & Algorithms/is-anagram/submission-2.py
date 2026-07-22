class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # base case 
            return False
        
        return sorted(s) == sorted(t)
        