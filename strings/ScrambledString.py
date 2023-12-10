class Solution(object):

      def isScrambled(self,s1,s2):

          if len(s1)!=len(s2):
              return False

          if len(s1) and len(s2) == 1:
              return True

          