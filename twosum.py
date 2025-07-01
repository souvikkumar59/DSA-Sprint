class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

        return {}




#t.c=O(n^2)
#s.c=O(1)# The above code is a brute force solution to the Two Sum problem.# It checks every pair of numbers in the list to see if they add up to the target.