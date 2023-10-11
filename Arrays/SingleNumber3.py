class Solution(object):
    def singleNumber(self, nums):

        count_dict = {}
        res =[]
        for num in nums:
            if num in count_dict:
               count_dict[num] += 1
            else:
               count_dict[num] = 1

        for num,count in count_dict.items():
            if count == 1:
                res.append(num)
            else:
                continue

        return res

if __name__ == '__main__':
    nums =[0,1]
    print(Solution().singleNumber(nums))
