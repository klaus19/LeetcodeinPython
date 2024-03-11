class Solution(object):
    def firstPalindrome(self, words):

        biggestString=""
        maxLen=0
        for word in words:
            l=0
            r=len(word)-1
            while l<=r:
                if word[l] == word[r]:
                    biggestString+=word
                    maxLen = max(maxLen,len(biggestString))
                else:
                    pass
            l+=1
            r-=1
        return biggestString

if __name__ == '__main__':
    words = ["abc", "car", "ada", "racecar", "cool"]
    print(Solution().firstPalindrome(words))