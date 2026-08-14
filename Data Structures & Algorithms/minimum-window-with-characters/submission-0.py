class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t : 
            return ""
        
        count = {}
        for c in t :
            count[c] = 1 + count.get(c, 0)
        l = 0
        need = len(count)
        have = 0 
        res = ""
        minlen = float("inf")
        for r in range(len(s)):
            window = {}





