class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count = {}

        for indx,char in enumerate(s):
            if char not in char_count: 
                char_count[char] = 1
            else:
                char_count[char]+=1
            
            if t[indx] not in char_count:
                char_count[t[indx]] = -1
            else:
                char_count[t[indx]] -=1

        if all(value == 0 for value in char_count.values()):
            return True
        return False
            