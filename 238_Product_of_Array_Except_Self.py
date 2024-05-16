class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [None for _ in range(len(nums))]
        # res stands for result

        leftProduct = 1
        for left_number in range(len(nums)):
            res[left_number] = leftProduct
            leftProduct *= nums[left_number]

        rightProduct = 1
        for right_number in range(len(nums)-1, -1, -1):
        # 3 '-1's stand for 'start, stop, step'
        # first len(nums)-1: start from the last element
        # second -1: end before the index 0
        # third -1: it's the step, means it will go reversely
            res[right_number] *= rightProduct
            rightProduct *= nums[right_number]

        return res