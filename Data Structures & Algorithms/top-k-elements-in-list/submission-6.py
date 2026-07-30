class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}      

        for i in range(len(nums))  :
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        
        count = []
        for key, values in freq.items():
            count.append([values, key])

        count.sort()
        li = []
        while len(li) < k :
            li.append(count.pop()[1])
        
        return li 









        














        
