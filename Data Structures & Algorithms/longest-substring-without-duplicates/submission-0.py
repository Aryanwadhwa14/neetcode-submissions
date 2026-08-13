class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0

        for l in range(len(s)) :
            ch = set()
            for r in range(l, len(s)):
                if s[r] in ch: 
                    break 
                ch.add(s[r])
            length = max(len(ch), length)
        return length 


