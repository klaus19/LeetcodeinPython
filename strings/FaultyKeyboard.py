class Solution(object):
    def finalString(self, s):

        result = ''
        for char in s:
            if char !='i':
                result +=char
            else:
                result = result[::-1]
        return result

if __name__ == "__main__":
    ss = "string"
    print(Solution().finalString(ss))