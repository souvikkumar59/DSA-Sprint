class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None
        for num in nums:
            if count==0:
                candidate=num
            if num==candidate:
                count+=1
            else:
                count-=1
        return candidate    
                
            







# t.c=O(n)# s.c=O(1)
# The above code is a solution to the problem of finding