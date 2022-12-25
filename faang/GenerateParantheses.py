class Solution(object):

    def generateParenthesis(self, n):

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        result = []
        backtrack("", 0, 0)
        return result


if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))
