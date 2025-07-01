class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        skb=set()
        for num in nums:
            if num in skb:
                return num
            else:
                skb.add(num)
        return -1        
    









# t.c=O(nlogn)
# s.c=O(n)
# The above code is a solution to the problem of finding a duplicate element in an array.

