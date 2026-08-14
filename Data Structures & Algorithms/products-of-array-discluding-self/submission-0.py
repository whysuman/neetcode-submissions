class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Lets start with the Prefix product array
        preprod = 1
        prefix = [1]
        for i in range(1,len(nums)):
            preprod *= nums[i - 1]
            prefix.append(preprod)
            print(f"For the current number: {nums[i]} the prefix product is: {preprod}")
        print(f"The preprod array is: {prefix}")

        # Now lets calculate the suffix product for each number 
        postprod = 1
        suffix = deque([])
        for i in range(len(nums) - 1,-1,-1):
            if i == len(nums) - 1:
                suffix.appendleft(1)
                continue
            postprod *= nums[i + 1]
            print(f"For the current number: {nums[i]} the postproduct is: {postprod}")
            suffix.appendleft(postprod)
        print(f"The suffix array: {suffix}")

        # Now we have to find the product of respective positions of prefix and suffix arrays
        final_res = []
        for i in range(len(nums)):
            final_res.append(prefix[i]*suffix[i])
        print(f"The final result is: {final_res}")
        return final_res