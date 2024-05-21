class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)

        # when the total number is 1 or 2, it's always True
        if n <= 2:
            return True

        # Initialize a counter to record how many times we encounter with a decreasing number
        count = 0

        for i in range(n-1):
            # When iterating the list and we meet a number which is greater than the following one
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:
                # if this is our second time meet that number
                    return False
                
                # if this is just the first time we meet a number that needs to be modified
                # the nums [0] is a individual situation, in this situation, we can solve by simply turn the first number into the second one and it'll be solved.
                # when nums[i] > nums[i + 1], there're only two conditions:1.nums[i-1]>nums[i+1] 2.nums[i-1]<nums[i+1]
                if i == 0 or nums[i - 1] <= nums[i + 1]:
                # The first situation, bring the nums[i] down.
                    nums[i] = nums[i + 1]
                else:
                # The second situation, bring the nums[i+1] up.
                    nums[i + 1] = nums[i]
        return True