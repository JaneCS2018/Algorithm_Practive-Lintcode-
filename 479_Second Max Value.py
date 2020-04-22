class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        maxval = max(nums[0], nums[1])
        sec = min(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            if nums[i]> maxval:
                sec = maxval
                maxval = nums[i]
            elif nums[i] > sec:
                sec = nums[i]
        return sec
                
