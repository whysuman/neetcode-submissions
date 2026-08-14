class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indx_map = new HashMap();
        int length = nums.length;
        for(int indx = 0; indx < length;indx++){
            int summand = target - nums[indx];
            if (indx_map.containsKey(summand)){
                int lower = indx_map.get(summand);
                return new int[]{lower,indx};
            }
            indx_map.put(nums[indx],indx);
        }
        
        return nums;
    }
}
