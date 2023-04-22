"""
Given an integer array nums, return true if any value 
appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

"""

class Solution:
    def contains_duplicate_using_set(self, nums: list[int]) -> bool:
        new_value = set(nums)
        
        if len(new_value) == len(nums):
            return False
        else:
            return True
        

class Solution:
    def contains_duplicate_using_binary_search(self, nums: list[int]) -> bool:

        nums.sort()
        for i in range(1, len(nums)):
            start = 0
            end = i - 1
            while start <= end:
                mid = (start + end) // 2
                if nums[i] == nums[mid]:
                    return True
                elif nums[i] < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return False