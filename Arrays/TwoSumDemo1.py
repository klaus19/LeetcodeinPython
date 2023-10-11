class Solution(object):

    def twoSum(self,nums,target):
        l=0
        r=len(nums)-1
        res = []

        while l <= r:
            if nums[l] + nums[r] ==target:
                res.append(l)
                res.append(r)
                break
            elif nums[l] + nums[r] <target:
                l+=1
            else:
                r-=1

        return res

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums,target))



