class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0]*26
        for i,value in enumerate(s):
            count[ord(value) - ord('a')]+=1
        
        for i,elem in enumerate(t):
            count[ord(elem) - ord('a')]-=1
        
        if count == [0]*26:
            return True
        else:
            return False
