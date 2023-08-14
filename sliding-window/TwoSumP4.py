
def twoSum(nums,target):

      num_dict={}

      for i ,num in enumerate(nums):
          complement = target-num

          if complement in num_dict:

              return [num_dict[complement],i]
          num_dict[complement]=i
          return