from typing import List

class Solution:
    def uniqueOccurrences(self,arr:List[int]) -> bool:
        counts = {}

        for i in arr:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        ocurrences = counts.values()
        unique_ocurrences = set(ocurrences)

        return len(ocurrences) == len(unique_ocurrences)

if __name__ == "__main__":
    solution = Solution()
    test_1 = [1,2,2,3,3,3]
    test_2 = [3,4,4,4,3,3]
    result_1 = solution.uniqueOcurrences(test_1)
    result_2 = solution.uniqueOcurrences(test_2)
    print(result_1,result_2)