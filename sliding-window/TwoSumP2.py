

def twoSum(self,nums,target):

    nums_doct = {}

    for i,num in enumerate(nums):
        complement = target-num
        if complement in nums_doct:

            return [nums_doct[complement],i]
        nums_doct[complement]=i
        return 