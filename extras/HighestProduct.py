class Solution(object):

    def maximum_product(self,lt):
     sorted(lt)
     curr_max = lt[0]
     max_product =lt[0]

     for i in range(1,len(lt)):
         curr_max = max(curr_max,lt[i]*curr_max,lt[i])
         max_product = curr_max

     return max_product

if __name__ == '__main__':
    lp = [10, -10, 5, 2]
    print(Solution().maximum_product(lp))