class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        res = defaultdict(list)
        for s in strs : 
            Sorted_s = "".join(sorted(s))
            res[Sorted_s].append(s)
        return list(res.values())
