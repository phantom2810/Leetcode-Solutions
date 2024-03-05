class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # First, sort the list in ascending order. This brings any duplicates next to each other.
        nums = sorted(nums)
        
        # Loop through the sorted list, stopping one element before the last
        for i in range(len(nums)-1):
            # Check if the current element is the same as the next one
            if nums[i] == nums[i+1]:
                # If a duplicate is found, return True
                return True
                
        # If the loop completes without finding duplicates, return False
        return False
