class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        index=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            else:
                nums[index]=nums[i]
                index+=1
        while count>0:
            nums[index]=0
            index+=1
            count-=1
        return nums
    
# t.c=O(n)
# s.c=O(1)