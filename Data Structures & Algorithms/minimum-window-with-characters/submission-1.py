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
        window = {}
       
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in count and count[c] == window[c] :
                have += 1
            while have == need :
                if r-l+1 < minlen :
                    minlen = r-l+1
                    res = s[l:r+1]
                
                window[s[l]] -= 1
                if s[l] in count and window[s[l]] < count[s[l]] :
                    have -= 1 
                l += 1
        return res



