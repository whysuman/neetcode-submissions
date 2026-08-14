class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            final_cnt = {}
            if len(strs) <= 1:
                return [strs]
                
            for string in strs:
                count = [0]*26
                for char in string:
                    # print(f"Current Character:{char} of Current String: {string}")
                    count[ord(char) - ord('a')] +=1 
                # print(f"Count is {count} of string: {string}")
                count = tuple(count)
                if count not in final_cnt:
                    final_cnt[tuple(count)] = [string]
                else:
                    final_cnt[count].append(string)
            return list(final_cnt.values())

