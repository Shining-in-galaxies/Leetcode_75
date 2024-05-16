class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Initialize two variables to infinity
        small_num_1 = float('inf')
        small_num_2 = float('inf')
        
        # Iterate through each element in the array
        for num in nums:
            if num <= small_num_1:
                # Update the smallest element if current number is smaller or equal
                small_num_1 = num
            elif num <= small_num_2:
                # Update the second smallest if current number is smaller or equal
                small_num_2 = num
            else:
                # Return True if a number is found that is greater than both small_num_1 and small_num_2
                return True
        
        # If no triplet found after iterating through the array, return False
        return False