from Arrays.MaximumCandies import Solution


class Solution:
    def checkIfPangram(self, sentence: str):
        return len(set(sentence)) == 26


if __name__ == "__main__":
    f = Solution()
    st = 'xyz'
    print(f.checkIfPangram(st))


