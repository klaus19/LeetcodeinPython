class Solution(object):

    def is_in_order(self, word):
        if word == "".join(sorted(word)):
            return True
        else:
            return False


if __name__ == "__main__":
    p = Solution()
    wtr = "2341"
    tre = "abc"
    print(p.is_in_order(wtr))
    print(p.is_in_order(tre))
