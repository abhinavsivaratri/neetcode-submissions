class Solution:
    def isValid(self, s: str) -> bool:
        paraenthesis_map = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in paraenthesis_map:
                stack.append(i)
            else:
                if stack and paraenthesis_map[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        return not stack


        