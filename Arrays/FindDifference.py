class Solution(object):
    def findTheDifference(self, s, t):
        str1 = list(s)
        str2 = list(t)
        str1.sort()
        str2.sort()

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                return str2[i]
        return str2[-1]


if __name__ == "__main__":
    s="abcd"
    t="abcde"
    print(Solution().findTheDifference(s, t))
