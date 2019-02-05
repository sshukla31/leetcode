'''
322. Coin Change
Medium

1314

66

Favorite

Share
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.


Refer:
https://www.youtube.com/watch?v=jgiZlGzXMBw

I used bottom-up approach
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # We will bottom-up approach

        # STEP 1:  Create an array dp to represent min coin required for each coin amount
        # First we will calculate best possible answer for each amount upto final amount
        # eg: amount = 11, so we will create an array of size amount+1
        # dp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # Then will fill the value of all with amount+1 as default
        # min_coins for each amount dp =  [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        # amount                           0 .  1 . 2 . 3   4 . 5 . 6 . 7 . 8   9 .10,  11

        # Note: This is same dp array where each index corresponds to amount and it value to
        #        minimum coins required

        dp = [amount+1] * (amount+1)
        dp[0] = 0


        # Step 2: Now calculate min coins for each amount trying all the available coins
        # eg: when i = 5 which means amount=5, we need to try all the available coins using
        # pointer j and get the min coin. Say we have coins 1,2,5  then we need only one coin
        # another example: amount = 3, then we can use only 1, 2. Here when we reach 2,
        # we do 3-2 = 1. Then we use dp to go dp[1] to know whats the min required for amount 1
        # Then we use that value + 1 for current coin 2, making it total=2
        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(
                        dp[i],
                        dp[i - coins[j]] + 1  # 1 means current coin and dp[i - coins[j]] means best val for remaining amount
                    )

        if dp[amount] > amount:
            return -1
        else:
            return dp[amount]


sol = Solution()
coins = [1, 2, 5]
amount = 11
expected_result = 3
actual_result = sol.coinChange(coins, amount)
assert actual_result == expected_result