from typing import List

class Solution:
    def findDifference(self,nums1:List[int], nums2:List[int]) -> List[List[int]]:
        h1 = set(nums1)
        h2 = set(nums2)
        
        list_1 = list(h1 - h2)
        list_2 = list(h2 - h1)

        answer = [list_1,list_2]

        return answer
    
if __name__ == "__main__":
    solution = Solution()
    test_1 = [4,5,5,6,9,0]
    test_2 = [7,0,8,2]
    result = solution.findDifference(test_1,test_2)
    print(result)