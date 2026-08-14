class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c for c in s if c.isalnum()).lower()
        s = s.lower()
        if len(s) <= 1:
            return True
        i,j = 0,len(s) - 1
        print(i,j)
        while i < j and s[i] == s[j]:
            i+=1
            j-=1
        print(i,j)
        if i < j:
            return False

        return True