class Solution:

    def encode(self, strs: List[str]) -> str:
        """ 
        Lets say the input is strs:[cars,mother,where,non-negotiable,#hero,#nah-bro#]
        if directely concatenate: carsmotherwhere....not possible to diffrentiate
        lets add a delimiter(#): cars#mother#where#non-negotiable##hero##nah-bro#
        Now how do we identify which # is the real delimiter in non-negotiable##hero##nah-bro#
        As we cant directly identify, lets add the string length directly after the delimiter # and before the word

        #4cars#6mother..#5#hero#8#nah-bro#

        NOW while decoding: if we encouter # and immediately a number,how do we know where to stop:
        for example lets say cars --> cars3 and mother --> 1 mother
        now --> 5#cars3#71mother --the algorithm wont know that 7 is the length,
        there lets swap # and the length

        --> 5#cars37#1mother we know 7 is the length as it ends with #, and weknow the strings at r in 1mother
        as we know the length of the string.


        """


        encoded_str = ""
        for string in strs:
            length = len(string)
            new_string = f"{length}#" + string
            encoded_str += new_string
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0                                                                                                                  
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result
        
        # result = []
        # temp = ""
        # str_flag = False
        # length = ""
        # for char in s:
        #     if length != 0 and str_flag:
        #         temp+=char
        #         length-=1
        #         if length == 0:
        #             result.append(temp)
        #             temp = ""
        #             length= ""
        #             str_flag = False
        #         continue
        #     if char.isdigit() and not str_flag:
        #         print(type(length),length)
        #         print(temp)
        #         length += char
        #         continue
        #     if char == "#":
        #         length = int(length)
        #         str_flag = True
        #         if length == 0:
        #             print("Visited")
        #             result.append("")
        #             length = ""
        #             str_flag = False
        #             temp = ""
        #             continue
        # return result    