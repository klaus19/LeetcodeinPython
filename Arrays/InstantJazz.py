class Solution:
 def jazz(self,items):
        return [item if '7' in item else item+'7' for item in items]



if __name__ == "__main__":
    p = Solution()
    lt = ['a7', 'g', 'u']
    print(p.jazz(lt))
