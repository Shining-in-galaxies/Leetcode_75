class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left <= right:
            mid = (left + right)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result > 0:
                left = mid + 1
            else:
                right = mid - 1
    