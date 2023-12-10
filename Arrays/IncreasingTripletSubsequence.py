class Solution(object):
    def increasingTriplet(self, nums):
        first,second = float('inf'),float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

if __name__ == '__main':
    arr = [1,2,3,4,5]
    print(Solution().increasingTriplet(arr))