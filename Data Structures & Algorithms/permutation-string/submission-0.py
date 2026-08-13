class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s = sorted(s1)
        for i in range(len(s2)):
            for j in range(i,len(s2)):
                subs = s2[i:j+1]
                t = sorted(subs)
                if t == s :
                    return True 
        return False 