class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char = {")":"(", "}":"{", "]":"["}
        
        for c in s : 
            if c in char : 
                if not stack or stack.pop() != char[c]:
                    return True
                else : 
                    stack.append(c)
        return stack == []
            
                