class Solution:
    def isPalindrome(self, s: str) -> bool:

        for char in s:
            if ord(char) not in range(65,91) and ord(char) not in range(97,123) and ord(char) not in range(48,58):
                s = s.replace(char,"")
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