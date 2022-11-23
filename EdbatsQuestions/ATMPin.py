class Solution(object):

    def validation(self, str):

        if len(str) == 6 or len(str) == 4:
            return True
        else:
            return False


if __name__ == "__main__":
    p = Solution()
    st = "1r456"
    rt = "1234"
    print(p.validation(st))
    print(p.validation(rt))
