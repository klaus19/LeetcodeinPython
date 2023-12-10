class Solution(object):
    def findRepeatedDnaSequences(self, s):

        id_names = set()
        st = ""
        left = 0
        count = 0
        result = set()

        for right in range(len(s)):
            st += s[right]
            count += 1

            if count == 10:
                if st not in id_names:
                    id_names.add(st)
                else:
                    result.add(st)

                # Move the sliding window to the right
                st = s[left + 1: right + 1]
                left += 1
                count -= 1

        return list(result)
if __name__ == "__main__":
   p= "AAAAAAAAAAAAA"
   print(Solution().findRepeatedDnaSequences(p))


