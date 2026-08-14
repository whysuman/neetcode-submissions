class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Creating a character frequency for each word
        freq_map = defaultdict(list)
        for idx,string in enumerate(strs):
            char_freq = [0]*26
            for char in string:
                char_freq[ord(char) - ord('a')]+=1
            freq_map[tuple(char_freq)].append(string)
        # print(freq_map)

        #Now appending all the grouped anagrams to the final list
        final_list = []
        for indx,value in enumerate(freq_map.values()):
            final_list.append(value)
        return final_list