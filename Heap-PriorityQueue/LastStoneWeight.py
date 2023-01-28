class Solution(object):

# lt=[2,7,4,1,8,1] , output =1

    def lastStoneWeight(self, stones):
        global second
        empty=[]

        if len(stones)==1:
            return stones[0]

        first = empty.append(max(stones))
        stones.remove(first)


        for i in range(len(stones)):
            second = max(stones)
            if stones[i]==second:
                del stones[i]
            empty.append(second)

        for j in range(0,len(empty)):
            diff = first-second
            stones.append(diff)

        return stones

if __name__ == "__main__":
    lt =[2,7,4,1,8,1]
    print(Solution().lastStoneWeight(lt))
