class Solution(object):
  def is_prime(self,num):
      if num <= 1:
          return False

      if num <= 3:
          return True

      for i in range(2, num):
          if (num % i) == 0:
              return False

      return True

if __name__ == "__main__":
    p = -1
    t = 6
    print(Solution().is_prime(p))
    print(Solution().is_prime(t))