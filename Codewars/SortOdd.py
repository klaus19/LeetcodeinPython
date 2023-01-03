class Solution(object):
   def sort_array(self,source_array):
       odd_numbers = sorted([n for n in source_array if n % 2 != 0])
       c = 0
       res = []
       for i in source_array:
           if i % 2 != 0:
               res.append(odd_numbers[c])
               c += 1
           else:
               res.append(i)
       return res

if __name__ == "__main__":
    pt = [5, 8, 6, 3, 4]
    print(Solution().sort_array(pt))



