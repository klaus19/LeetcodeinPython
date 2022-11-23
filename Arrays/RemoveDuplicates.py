class Solution(object):

    def deleteDuplicates(self, head):
        unique = set(head)
        return unique


if __name__ == "__main__":
    p = Solution()
    he = [2, 3, 5, 6, 5]
    print(p.deleteDuplicates(he))
