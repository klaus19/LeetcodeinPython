class Solution(object):
  def two_sum(self,nums, target):

#[1, 2, 3, 4, 5]
    res =[]
    find = nums[0]
    for i in range(1,len(nums)):
          if target-nums[i] ==find:
              return True
          else:
              pass

    return True

if __name__ == '__main__':
    lt =[1, 3, 5]
    tar = 5
    print(Solution().two_sum(lt,tar))
