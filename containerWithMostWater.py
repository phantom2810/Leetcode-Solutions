class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize left and right pointers, and max_area variable
        left, right = 0, len(height) - 1
        max_area = 0
        
        # Loop until the two pointers meet
        while left < right:
            # Calculate the current area
            current_area = (right - left) * min(height[left], height[right])
            # Update max_area if current_area is larger
            max_area = max(max_area, current_area)
            
            # Move the pointer for the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
