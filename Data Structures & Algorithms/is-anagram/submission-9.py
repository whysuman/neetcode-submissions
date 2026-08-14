class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sorted_s = {}
        sorted_t = {}
        for i in range(len(s)):
            sorted_s[s[i]] = sorted_s.get(s[i],0) + 1
            sorted_t[t[i]] = sorted_t.get(t[i],0) + 1
        
        return sorted_s == sorted_t

