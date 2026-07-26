class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = [[] for i in nums+1]
        
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        for key, value in freq.items():
            res[value].append(key)

        li = []   
        for i in range(len(res)-1, 0, -1):
            for num in res[i]:
                li.append(num)
                if len(li) == k :
                    return li








        














        
