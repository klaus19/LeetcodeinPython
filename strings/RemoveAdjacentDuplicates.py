class Solution(object):
    def removeDuplicates(self, s):
        stack =[]
        for chara in s:
            if stack and stack[-1] == chara:
                stack.pop()
                continue
            stack.append(chara)
        return "".join(stack)

if __name__ == "__main__":
    s = "abbaca"
    print(Solution().removeDuplicates(s))