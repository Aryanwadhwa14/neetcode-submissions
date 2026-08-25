class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        count, window = {}, {}
        for i in s:
            count[i] = 1 + count.get(i, 0)
        for j in t : 
            window[j] = 1 + window.get(j, 0)
    
        if count == window : 
            return True 
        return False 
