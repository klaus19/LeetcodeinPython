class Solution(object):
    def makePalindrome(self, s):
        count=0
        l=0
        r=len(s)-1
        s_list = list(s)

        while l<=r:
           if s_list[l] ==s_list[r]:
               l+=1
               r-=1
           else:
               s_list[l]=s_list[r]
               count+=1
               l+=1
               r-=1

               if count>2:
                   return False
        return True

if __name__ == "__main__":
    s = "abcdba"
    print(Solution().makePalindrome(s))

