
class Solution(object):
  def listcheck(self,nums):
      nums.pop(0)
      nums.pop(-1)


if __name__ == "__main__":

    pt=[1,2]
    print(Solution().listcheck(pt))
