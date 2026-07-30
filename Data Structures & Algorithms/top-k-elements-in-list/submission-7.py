class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}      
        count  = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums))  :
            freq[nums[i]] = 1 + freq.get(nums[i], 0)
        
        for key, values in freq.items():
            count[values].append(key)
        
        res = []
        for i in range(len(count)-1,-1,-1):
            for num in count[i] :
                res.append(num)
                if len(res) == k :
                    return res 
    



        
        
        









        














        
