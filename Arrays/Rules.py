class Solution(object):

     def Rule(self, list=[], str=""):

         if str == "Asc":
          return list.sort()
         elif str == "Des":
          return list.sort(reverse=True)
         else:
          return list

         if __name__ == "__main__":
            p = Solution()
            li=[3,1,6,7]
            print(p.Rule(li,str="Asc"))
