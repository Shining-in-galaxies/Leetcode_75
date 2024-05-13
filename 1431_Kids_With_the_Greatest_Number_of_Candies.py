class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for current_candies in candies:
            if (current_candies + extraCandies) >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result