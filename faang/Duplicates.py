class Solution(object):

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ltr = set(nums)

        if len(nums) == len(ltr):
            return True

        else:
            return False


if __name__ == "__main__":

    l1=[1,3,4,2]
    print(Solution().containsDuplicate(l1))
