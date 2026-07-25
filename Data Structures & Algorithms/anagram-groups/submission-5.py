class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        seen = defaultdict(list)
        for s in strs : 
            count = [0]*26 
            for ch in s : 
                count[ord(ch) - ord("a")] += 1
            seen[tuple(count)].append(s)
        return list(seen.values()) # without solution reading 

        
