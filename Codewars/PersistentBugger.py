class Solution(object):

    def persistence(self,num):


        while num > 9:

            num_str = str(num)
            total = 1
            for i in num_str:
                total = total * int(i)
            num = total
        return num

if __name__ == "__main__":
    p = 4
    print(Solution().persistence(p))