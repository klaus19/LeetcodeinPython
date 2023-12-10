class Solution(object):
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2  = len(word2)

        dp = [[-1] * (len2+1) for _ in range(len1+1)]


        for i in range(len1+1):
            for j in range(len2+1):
                # if word1 is empty
                if i ==0:
                    dp[i][j] = j
                # if word2 is empty
                elif j ==0:
                    dp[i][j] = i
                # if both words are same
                elif word1[i-1] == word2[j-1]:
                    dp[i][j] = dp [i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
        return dp[len1][len2]


if __name__ == '__main__':
    word1 = "horse"
    word2 = "ros"
    print(Solution().minDistance(word1,word2))