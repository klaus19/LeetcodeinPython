class Solution(object):

    def birthdayCakeCandles(self,candles):

        if len(candles)==1:
            return candles[0]

        candles.sort()
        end = len(candles)-1
        curr_max=candles[end]
        count=1

        while end >0 and candles[end-1] == curr_max:
             count+=1
             end-=1
        return count

if __name__ == "__main__":
    nums = [3,2,1,3,3]
    print(Solution().birthdayCakeCandles(nums))
