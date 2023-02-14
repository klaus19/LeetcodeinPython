class Solution(object):

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0


        # Check if num is divisible by any number from 2 to num-1

        for num in range(2,n):
            isPrime = True
            # Check if num is divisible by any number from 2 to num-1
            for i in range(2,num-1):
                if num % i == 0:
                    is_prime = False
                    break
                    # If num is prime, increment the count
                if is_prime:
                    count += 1
                return count