class Solution:
    def reverseWords(self, s: str) -> str:
        m = s.split()
        n = reversed(m)
        return " ".join(n)