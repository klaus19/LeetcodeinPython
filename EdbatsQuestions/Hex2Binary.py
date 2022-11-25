class Solution(object):

    def hex_to_binary(self, hexvalue):
        bin_value = bin(hexvalue)
        return bin_value


if __name__ == "__main__":
    p = Solution()
    tr = 0xAA
    print(p.hex_to_binary(tr))
