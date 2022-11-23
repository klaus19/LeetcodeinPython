class Solution:
    def search(self, nums, target):

        for i in range(len(nums)):
            if target in nums:
                return True
            else:
                return False


if __name__ == "__main__":
    p = Solution()
    no = [2, 5, 6, 0, 0, 1, 2]
    li = [2,5,6,0,0,1,2]
    mat=3
    tar = 0
    print(p.search(no, tar))
    print(p.search(li,mat))

