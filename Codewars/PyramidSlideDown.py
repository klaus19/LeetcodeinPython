
class Solution(object):

  def longest_slide_down(self,pyramid):
    # TODO: write some code...

    sum=0

    i=len(pyramid)-1
    while i>=0:
          sum+=pyramid[i]-1
          i = i-1
    return sum

if __name__ == "__main__":

    pt = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    print(Solution().longest_slide_down(pt))