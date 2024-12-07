from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_weight = 0
        right_weight = sum(nums)

        for indx, current_weight in enumerate(nums):
            left_weight += current_weight
            if left_weight == right_weight:
                return indx
            right_weight -= current_weight

        return -1

if __name__ == "__main__":
    solution = Solution()
    test_1 = [7,9,11,3,0,-4]
    test_2 = [1, 7, 3, 6, 5, 6]
    result_1 = solution.pivotIndex(test_1)
    result_2 = solution.pivotIndex(test_2)
    print(result_1)
    print(result_2)
