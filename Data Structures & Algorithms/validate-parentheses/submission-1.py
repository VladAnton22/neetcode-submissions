class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")": "(", 
            "}": "{", 
            "]": "["
            }
        opening_brackets = {"(", "{", "["}
        stack = []

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in pairs:
                if len(stack) == 0:
                    return False
                if pairs[char] != stack[-1]:
                    return False
                stack.pop()

        if len(stack) == 0:
            return True
        else:
            return False