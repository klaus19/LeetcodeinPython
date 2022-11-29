class Solution(object):

    def find_issue(self, dic, key):

        if key in dic:
            print(key + " " + "is gone...")
        else:
            print(key + " " + "is here!")


if __name__ == "__main__":
    p = Solution()
    d = {
        "tejas", 34,
        "niks", 20,
        "ro", 67
    }
    k = "tejas"
    print(p.find_issue(d, k))
