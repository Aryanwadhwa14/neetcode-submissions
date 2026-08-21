class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        length = 0
        ch = set()

        for r in range(len(s)):
            while s[r] in ch:
                ch.remove(s[l])
                l += 1
            ch.add(s[r])
            length = max(len(ch), length)
        return length



