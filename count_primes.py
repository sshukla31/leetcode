'''
204. Count Primes
Easy

1534

509

Add to List

Share
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

'''
Sieve of Eratosthenes algo
'''

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0


        # assume all no's are prime. we use 1 instead of bool, as we can use sum()
        # to get count of all primes easily
        primes = [1] * n
        primes[0] = primes[1] = 0


        #for i in range(2, int(n ** 0.5) + 1):
        for i in range(2, int(math.floor(math.sqrt(n))) + 1):
            # n ** 0.5 == sqrt(n) here, so when we pass 9, we only look for 3.0
            # we can also use math.sqrt, which will round up with floor to give same result
            # even if sqrt(n) is not prime, then n is not prime
            # we don't have to check for n
            if primes[i] == 1:
                # note: multiple of primes are NOT prime: eg: 2 is prime , 4 is not
                for j in range(i*i, n, i):
                    primes[j] = 0

        return sum(primes)



sol = Solution()
assert 4 == sol.countPrimes(10)
assert 25 == sol.countPrimes(100)
assert 11 == sol.countPrimes(34)
assert 0 == sol.countPrimes(2)