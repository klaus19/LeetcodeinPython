class Solution(object):

    def odd_or_even(self,arr):
        sum_arr=0
        ans=''
        for i in range(len(arr)):
            sum_arr +=arr[i]
            if sum_arr %2 !=0:
                ans ="".join('odd')
            else:
                ans = "".join('even')
        return ans

if __name__ == '__main__':
    lt = [0,1,4]
    l=[0]
    print(Solution().odd_or_even(lt))
    print(Solution().odd_or_even(l))

