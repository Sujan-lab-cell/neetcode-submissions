class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=""
        for strs in s:
            if strs.isalnum():
                result+=strs.lower()
            else:
                continue
        return result==result[::-1]
