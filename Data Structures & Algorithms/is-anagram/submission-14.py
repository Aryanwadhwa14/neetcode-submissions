class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        # brute forces -> using sort function 
        return sorted(s) == sorted(t)