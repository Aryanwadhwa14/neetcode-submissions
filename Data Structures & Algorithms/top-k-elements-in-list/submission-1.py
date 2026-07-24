class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            res[i] = 1 + res.get(i,0)
        
        freq = []
        for key, value in res.items():
            freq.append([value, key])
        freq.sort()

        li = []
        while len(li) < k:
            pp = freq.pop()[1]
            li.append(pp)

        return li








        
