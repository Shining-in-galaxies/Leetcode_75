import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2) == (str2 + str1):
            len_of_gcd = math.gcd(len(str1),len(str2))
            return str1[0:len_of_gcd]
        return ""