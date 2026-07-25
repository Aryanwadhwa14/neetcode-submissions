class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        freq = [[] for i in range(len(nums)+1)]

        for s in nums:
            res[s] = 1 + res.get(s, 0) 

        for key, value in res.items():
            freq[value].append(key)

        li = []
        for i in range(len(freq)-1, 0,-1): 
            for j in freq[i]:  
                li.append(j)
                if len(li) == k : 
                    return li












        
