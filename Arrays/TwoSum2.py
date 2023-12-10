class Solution(object):

    def twoSum2(self,numbers,target):

        left, right = 0,len(numbers)-1

        while left < right:
            curr_sum = numbers[left]+numbers[right]

            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum > target:
                right-=1
            else:
                left+=1

if __name__ == '__main__':
    res = [3,5,6,7]
    target = 11
    print(Solution().twoSum2(res,target))