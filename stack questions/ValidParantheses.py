class Solution(object):

    def validParanthesis(self,s):



        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if not stack:
                    return False
                top = stack.pop()
                if c == ")" and top != "(":
                    return False
                elif c == "]" and top != "[":
                    return False
                elif c == "}" and top != "{":
                    return False
        return not stack

if __name__ == "__main__":
    stt = "{}"
    print(Solution().validParanthesis(stt))
