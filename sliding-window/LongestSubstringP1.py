class Solution(object):

    def longestSubstring(self,s):

        char_set = set()
        count =0
        left=0
        right = 0

        while right <len(s):

            if s[right] not in char_set:

                char_set.add(s[right])
                count = max(count,right-left+1)
                right+=1
            else:
                char_set.remove(s[right])
                left+=1

        return count

if __name__ == "__main__":
    S="abcdaa"
    print(Solution().longestSubstring(S))


