class Solution(object):
    def containSuplicate3(self,nums,indexDiff,valueDiff):
        i=0
        j=1

        while j <len(nums):
            if i!=j and abs(i-j) <=indexDiff and abs(nums[i]-nums[j]) <=valueDiff:
                return True
            else:
                j+=1
        i+=1
        return False

if __name__ == '__main__':
    nums = [1,2,1,1]
    indexDiff = 1
    valueDiff = 0
    print(Solution().containSuplicate3(nums,indexDiff,valueDiff))