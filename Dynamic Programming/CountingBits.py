class Solution(object):

    def countBits(self, num: int):
        counter = [0]
        for i in range(1, num + 1):
            counter.append(counter[i >> 1] + i % 2)
        return counter

if __name__ == '__main__':
    n=2
    print(Solution().countBits(n))