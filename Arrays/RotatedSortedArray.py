class Solution:

    def rotateArray(self,nums,target):

        try:
            return nums.index(target)
        except:
            return -1