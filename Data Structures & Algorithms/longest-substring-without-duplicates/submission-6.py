class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        res = 0 
        ch = set()

        for r in range(len(s)): 
            while s[r] in ch : 
                ch.remove(s[l])
                l += 1 
            ch.add(s[r])
            res = max(res, len(ch))
        return res 



