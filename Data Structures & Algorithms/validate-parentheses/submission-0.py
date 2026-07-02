class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in {"(","{","["} or not stack:
                stack.append(c)
            else:
                if c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    stack.append(c)
        return False if stack else True