class Solution(object):

    def minmax(self,nums):
        nums.sort()
        minimum_number = nums[0]
        maximum_number = nums[-1]
        res=[]
        j=1
        count = 0
        while count!=1:
            if minimum_number+j in nums:
                  pass

            else:
                  res.append(minimum_number)
                  res.append(minimum_number + j)
                  res.append(maximum_number)
                  count += 1
            j += 1
        return res

    def second_solution(self,arr):
            arr = sorted(set(arr))
            for i, x in enumerate(arr, arr[0]):
                if i != x:
                    return [arr[0], i, arr[-1]]

if __name__ == "__main__":
    pt = [2, -4, 8, -5, 9, 7]
    lt = [1, 3, -3, -2, 8, -1]
    print(Solution().minmax(pt))
    print(Solution().minmax(lt))