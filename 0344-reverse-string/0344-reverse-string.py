class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        #s[:] = s[::-1] #Both works.
