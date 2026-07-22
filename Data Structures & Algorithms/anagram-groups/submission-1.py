
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s: 
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())

                # [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1] -> act
                # "act" ->  a - a = 0 : 1
                # c -> 99 - 97 =   2 : 1
                # t -> 116 - 97 = 19 : 1

            

        