class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        count=0
        if len(s)==0:
            return 0
        for  i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
                continue
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    count = max(count, i - stack[-1])
        return count
        
            
            
        