class Solution(object):

    def  hamming(self,n):
         return bin(n).count('1')

if __name__ == '__main__':
    n= 0o0000000000000000000000010000000
    nt = 0o0000000000000000000000000001011
    print(Solution().hamming(n))
    print(Solution().hamming(nt))