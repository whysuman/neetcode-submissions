class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(set(s)) == 1:
            return True

        j = len(s) - 1
        for i in range(len(s)):
            print(s[i],s[j])
            if j <= i:
                return True
            if s[i].isalnum() == False:
                continue
            if s[j].isalnum() == False:
                while not s[j].isalnum():
                    j-=1

            print("After: ",s[i],s[j])
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1

        
    
        