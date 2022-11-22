class Solution(object):

    def stutter(self, str):
        st = str[:2]
        rev = ""
        rev += st + '...' + st + '...' + str + '?'
        return rev


if __name__ == "__main__":
    p = Solution()
    s = "incredible"
    print(p.stutter(s))
